from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists, isdir
from os import listdir, walk, remove, makedirs
import shutil


class Command(BaseCommand):
    help = "Clean Project"
    DANGER_FOLDERS_LIST = (
        "Database",
        "media",
        "static",
        "templates",
        "venv",
        "node_modules",
        "env",
        "virtualenv",
        "virtualEnv",
        "vEnv",
        "Assets",
        "venv",
        "Assets",
        "test",
        "Scripts",
        "bin",
        "lib",
        "include",
        "share",
        "src",
        "dist",
        "build",
        "node_modules",
        "public",
        "static",
        "media",
        "templates",
        ".idea",
        ".git",
    )

    def handle(self, *args, **options):
        self.delete_database()
        self.delete_static_root()
        self.clean_migrations()
        self.create_media_folders()

    def delete_database(self):
        if exists(join(settings.BASE_DIR, "Database")):
            shutil.rmtree(join(settings.BASE_DIR, "Database"))
        makedirs(join(settings.BASE_DIR, "Database"), exist_ok=True)

    def delete_static_root(self):
        if exists(settings.STATIC_ROOT):
            shutil.rmtree(settings.STATIC_ROOT)
        makedirs(settings.STATIC_ROOT, exist_ok=True)

    def clean_migrations(self):
        for item in listdir(settings.BASE_DIR):
            if (
                isdir(join(settings.BASE_DIR, item))
                and item not in self.DANGER_FOLDERS_LIST
            ):
                self.delete__pycache__(join(settings.BASE_DIR, item))
                self.stdout.write(
                    self.style.WARNING(f"Start Delete Migrations in App {item}")
                )
                if exists(join(settings.BASE_DIR, item, "migrations")):
                    for file in listdir(join(settings.BASE_DIR, item, "migrations")):
                        if file not in ["__init__.py"]:
                            try:
                                remove(
                                    join(settings.BASE_DIR, item, "migrations", file)
                                )
                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f"Successfully Delete {join(settings.BASE_DIR, item, 'migrations', file)}"
                                    )
                                )
                            except Exception as e:
                                self.stdout.write(
                                    self.style.ERROR(
                                        f"Delete Migrations {join(settings.BASE_DIR, item, 'migrations', file)} Error is >>> {e}"
                                    )
                                )

    def delete__pycache__(self, path_dir: str):
        self.style.WARNING(f"Delete __pycache__ in App {path_dir}")
        for dirpath, dirnames, filenames in walk(path_dir):
            for p in dirnames:
                if str(p).endswith("__pycache__"):
                    try:
                        shutil.rmtree(join(dirpath, p))
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully Delete __pycache__ in Path {join(dirpath, p)}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Delete __pycache__ in Path {join(dirpath, p)} Error is >>> {e}"
                            )
                        )

    def create_media_folders(self):
        media_files = [
            "images",
            "sounds",
            "videos",
            "svg",
        ]
        for media_file in media_files:
            if not exists(join(settings.MEDIA_ROOT, media_file)):
                makedirs(join(settings.MEDIA_ROOT, media_file), exist_ok=True)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully Create Folder>> {join(settings.MEDIA_ROOT, media_file)}"
                    )
                )
