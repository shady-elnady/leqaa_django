from django.core.management.base import BaseCommand
from django.conf import settings
from firebase_admin import auth


class Command(BaseCommand):
    help = "Seeds the database and deletes all Firebase Authentication users"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(
                "Starting data seeding and Firebase Authentication user cleanup..."
            )
        )

        try:
            # Initialize Firebase Admin SDK if not already initialized
            if not settings.FIREBASE_ADMIN_SDK_INITIALIZED:
                self.stdout.write(
                    self.style.ERROR("Failed Firebase Admin SDK initialized.")
                )

            # List all users in Firebase Authentication
            users = auth.list_users()
            deleted_count = 0

            for user in users.iterate_all():
                try:
                    auth.delete_user(user.uid)
                    deleted_count += 1
                    self.stdout.write(self.style.SUCCESS(f"Deleted user: {user.uid}"))
                except Exception as e:
                    self.stderr.write(
                        self.style.ERROR(f"Error deleting user {user.uid}: {e}")
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully deleted {deleted_count} users from Firebase Authentication."
                )
            )

            # Your seeding logic goes here
            self.stdout.write(self.style.SUCCESS("Data seeding completed."))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))

        self.stdout.write(
            self.style.SUCCESS(
                "Finished data seeding and Firebase Authentication user cleanup."
            )
        )
