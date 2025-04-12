from django.db.models import (
    Model,
    ImageField,
    URLField,
)
from firebase_admin import storage, exceptions as firebase_exceptions
from django.conf import settings
from os.path import join, exists
from urllib.parse import quote
import logging
import os

from .tools.upload_image import upload_image_to
from App.messages import FieldsMessages, AuthMessages


logger = logging.getLogger(__name__)


class BaseImageModel(Model):
    """
    Abstract base model for handling image uploads to both local storage and Firebase.
    Automatically manages uploads, deletions, and URL management.
    """

    image = ImageField(
        upload_to=upload_image_to,
        null=True,
        blank=True,
        verbose_name=FieldsMessages.IMAGE,
    )
    firebase_image_url = URLField(
        blank=True,
        null=True,
        editable=False,
        verbose_name=AuthMessages.FIREBASE_IMAGE_URL,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Save the model instance and handle image upload to Firebase.
        """
        is_new_image = False

        if self.image and (not self.pk or self._state.adding):
            is_new_image = True

        super().save(*args, **kwargs)  # Save first to get the PK

        if is_new_image:
            try:
                self._upload_image_to_firebase()
                # Update only the firebase_image_url field
                super().save(update_fields=["firebase_image_url"])
            except Exception as e:
                logger.error(f"Failed to upload image to Firebase: {e}")
                # Clean up the local file if Firebase upload fails
                if self.image and exists(self.image.path):
                    os.remove(self.image.path)
                raise

    def _upload_image_to_firebase(self):
        """
        Upload the image to Firebase Storage and set the public URL.
        """
        if not self.image:
            return

        bucket_name = settings.FIREBASE_STORAGE_BUCKET
        if not bucket_name:
            raise ValueError("FIREBASE_STORAGE_BUCKET not configured in settings")

        try:
            bucket = storage.bucket(bucket_name)
            file_path = self.image.name
            blob = bucket.blob(file_path)

            # Upload the file
            blob.upload_from_filename(self.image.path)

            # Set public access
            blob.make_public()

            # Store the public URL
            self.firebase_image_url = blob.public_url

            # Optionally delete local file after successful upload
            # if exists(self.image.path):
            #     os.remove(self.image.path)

        except firebase_exceptions.FirebaseError as e:
            logger.error(f"Firebase error during image upload: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during Firebase upload: {e}")
            raise

    def _get_firebase_image_url(self):
        """
        Generate the Firebase Storage URL for the image.
        """
        if not self.image or not self.image.name:
            return None

        bucket_name = settings.FIREBASE_STORAGE_BUCKET
        if not bucket_name:
            return None

        # Properly encode the file path for URL
        encoded_path = quote(self.image.name)
        return f"https://firebasestorage.googleapis.com/v0/b/{bucket_name}/o/{encoded_path}?alt=media"

    def delete(self, *args, **kwargs):
        """
        Delete the instance along with its associated files from both local storage and Firebase.
        """
        if self.image:
            self._delete_local_file()
            self._delete_firebase_file()
        super().delete(*args, **kwargs)

    def _delete_local_file(self):
        """
        Delete the local image file.
        """
        if self.image and exists(self.image.path):
            try:
                os.remove(self.image.path)
            except OSError as e:
                logger.error(f"Error deleting local image file: {e}")

    def _delete_firebase_file(self):
        """
        Delete the image file from Firebase Storage.
        """
        if not self.image or not self.image.name:
            return

        bucket_name = settings.FIREBASE_STORAGE_BUCKET
        if not bucket_name:
            return

        try:
            bucket = storage.bucket(bucket_name)
            blob = bucket.blob(self.image.name)
            blob.delete()
        except firebase_exceptions.NotFound:
            logger.warning(
                f"Firebase file not found during deletion: {self.image.name}"
            )
        except firebase_exceptions.FirebaseError as e:
            logger.error(f"Firebase error during file deletion: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during Firebase deletion: {e}")

    def clean(self):
        """
        Validate the model before saving.
        """
        super().clean()

        if self.image and not self.pk:
            # Verify Firebase is initialized
            try:
                storage.bucket()
            except (ValueError, AttributeError) as e:
                raise ValueError(
                    "Firebase Admin SDK not properly initialized. Please check your settings."
                )

            # Clean up any existing file if validation fails
            if exists(self.image.path):
                try:
                    os.remove(self.image.path)
                except OSError as e:
                    logger.error(f"Error cleaning up image file during validation: {e}")
