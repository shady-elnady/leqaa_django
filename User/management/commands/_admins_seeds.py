from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists, isabs, splitext, basename
from os import makedirs, listdir
from django.core.files import File
from django.core.files.storage import default_storage

from Currency.models import Currency
from Locale.models import Language
from User.models import User, UserAlbum, Profile
from User.utils.enums import USERS_TYPES, TITLES, GENDERS


class Command(BaseCommand):
    help = "Create Initial Admins Load Data"

    def handle(self, *args, **options):

        image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")
        APP_DIR = join(settings.BASE_DIR, "User")

        admins_albums_images_directory = join(IMAGES_ROOT, "Users Albums", "Admins")
        if not exists(admins_albums_images_directory):
            makedirs(admins_albums_images_directory, exist_ok=True)

        admins_profile_avatars_directory = join(IMAGES_ROOT, "Avatars", "Admins")
        if not exists(admins_profile_avatars_directory):
            makedirs(admins_profile_avatars_directory, exist_ok=True)

        admins = [
            {
                "username": "Shady",
                "email": "shady@g.com",
                "password": "12345678",
                "user_type": USERS_TYPES.Admin,
                "mobile": "+201000000000",
                "Profile": {
                    "full_name": "شادى رافت سعد",
                    "national_id": "01111111111111",
                    "birth_date": None,
                    "title": TITLES.Doctor,
                    "gender": GENDERS.MALE,
                    "university_number": "01111111111111",
                    "is_graduate": False,
                    "currency": 1,
                    "language": 1,
                    "avatar": "Shady.png",
                    "contact_info": {
                        "Telephone": "+2 050 5060570",
                        "lat": 4.33333,
                        "lng": 4.33333,
                    },
                },
            },
        ]
        for admin in admins:
            try:
                admin_instance: User = User.objects.create_admin(
                    username=admin["username"],
                    email=admin["email"],
                    password=admin["password"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully  Create Admins with Name > {admin['username']}"
                    )
                )
                try:
                    ADMIN_PROFILE_AVATAR = join(
                        admins_profile_avatars_directory,
                        f"{admin_instance.id}.png",
                    )
                    Profile.objects.update_or_create(
                        user=admin_instance,
                        defaults={
                            "avatar": ADMIN_PROFILE_AVATAR,
                            "national_id": admin["Profile"]["national_id"],
                            "full_name": admin["Profile"]["full_name"],
                            "birth_date": admin["Profile"]["birth_date"],
                            "title": admin["Profile"]["title"],
                            "gender": admin["Profile"]["gender"],
                            "university_number": admin["Profile"]["university_number"],
                            "is_graduate": admin["Profile"]["is_graduate"],
                            "currency": Currency.objects.get(
                                pk=admin["Profile"]["currency"]
                            ),
                            "language": Language.objects.get(
                                pk=admin["Profile"]["language"]
                            ),
                            "contact_info": admin["Profile"]["contact_info"],
                        },
                    )
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully  Create Admins Profile with Name > {admin['username']}"
                        )
                    )
                    self.copy_image_with_new_name(
                        old_image_path=join(
                            APP_DIR,
                            "management",
                            "media",
                            "Images",
                            "Avatars",
                            "Admins",
                            admin["Profile"]["avatar"],
                        ),
                        new_directory=admins_profile_avatars_directory,
                        new_filename=f"{admin_instance.id}",
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Failed Create Admins Profile with Name > {admin['username']} , \n \t Error is: \t \t{e}"
                        )
                    )
                for filename in listdir(
                    join(
                        APP_DIR,
                        "management",
                        "media",
                        "Images",
                        "Users Albums",
                        "Admins",
                        username=admin["username"],
                    )
                ):
                    if any(filename.lower().endswith(ext) for ext in image_extensions):
                        try:
                            UserAlbum.objects.create(
                                user=admin_instance,
                                photo=join(
                                    admins_albums_images_directory,
                                    f"{admin_instance.id}",
                                    f"{id}.png",
                                ),
                            )
                            self.stdout.write(
                                self.style.SUCCESS(
                                    f"Successfully  Create Photo for Admins with Name > {admin_instance.username}"
                                )
                            )
                            self.copy_image_with_new_name(
                                old_image_path=join(
                                    APP_DIR,
                                    "management",
                                    "media",
                                    "Images",
                                    "Users Albums",
                                    "Admins",
                                    username=admin["username"],
                                ),
                                new_directory=admins_profile_avatars_directory,
                                new_filename=f"{admin_instance.id}",
                            )
                        except Exception as e:
                            self.stdout.write(
                                self.style.ERROR(
                                    f"Failed Create Photo for Admins with Name > {admin_instance.username} , \n \t Error is: \t \t{e}"
                                )
                            )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create User with Name > {admin['username']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Admins Load Data"))

    def copy_image_with_new_name(
        self, old_image_path, new_directory, new_filename=None
    ):
        """
        Copies an image from an old path to a new path with an optional new name.

        Args:
            old_image_path (str): The absolute path to the old image file.
            new_directory (str): The directory where the new image will be saved.
                            This path should be relative to your MEDIA_ROOT or an absolute path.
            new_filename (str, optional): The desired name for the new image file (without extension).
                                        If None, the original filename (without extension) is used.
                                        Defaults to None.

        Returns:
            str or None: The full path to the new image file if successful, otherwise None.
        """
        if not exists(old_image_path):
            self.stdout.write(
                self.style.ERROR(f"Error: Old image path not found: {old_image_path}")
            )
            return None

        if not exists(new_directory):
            makedirs(new_directory, exist_ok=True)

        if not isabs(new_directory) and not new_directory.startswith(
            settings.MEDIA_URL
        ):
            new_directory = join(settings.MEDIA_ROOT, new_directory)

        try:
            with open(old_image_path, "rb") as f:
                file = File(f)
                base_name, ext = splitext(basename(old_image_path))

                if new_filename:
                    new_name_with_ext = f"{new_filename}{ext.lower()}"
                else:
                    new_name_with_ext = f"{base_name}{ext.lower()}"

                new_file_path = join(new_directory, new_name_with_ext)

                # Save the file to the new location
                default_storage.save(new_file_path, file)

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Success copying Image from {old_image_path} to {new_directory}"
                    )
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    f"Error copying Image from {old_image_path} to {new_directory}: {e}"
                )
            )
