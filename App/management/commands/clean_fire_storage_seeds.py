from django.core.management.base import BaseCommand
from django.conf import settings
from firebase_admin import storage


class Command(BaseCommand):
    help = "Seeds the database and deletes old Firebase Storage files"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Starting data seeding and Firebase file cleanup...")
        )

        try:
            # Initialize Firebase Admin SDK if not already initialized
            if not settings.FIREBASE_ADMIN_SDK_INITIALIZED:
                self.stdout.write(
                    self.style.ERROR("Failed Firebase Admin SDK initialized.")
                )

            bucket = storage.bucket()

            # List all files in the bucket
            blobs = bucket.list_blobs()
            deleted_count = 0

            for blob in blobs:
                try:
                    blob.delete()
                    deleted_count += 1
                    self.stdout.write(self.style.SUCCESS(f"Deleted file: {blob.name}"))
                except Exception as e:
                    self.stderr.write(
                        self.style.ERROR(f"Error deleting file {blob.name}: {e}")
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully deleted {deleted_count} files from Firebase Storage."
                )
            )

            # Your seeding logic goes here
            self.stdout.write(self.style.SUCCESS("Data seeding completed."))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))

        self.stdout.write(
            self.style.SUCCESS("Finished data seeding and Firebase file cleanup.")
        )
