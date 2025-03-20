from django.core.management.base import BaseCommand

from Favorite.models import Favorite
from User.models import User
from Event.models import Event


class Command(BaseCommand):
    data = "Favorites"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        favorites = [
            {
                "user": 1,
                "event": 1,
            },
            {
                "user": 1,
                "event": 2,
            },
            {
                "user": 2,
                "event": 3,
            },
            {
                "user": 3,
                "event": 4,
            },
            {
                "user": 4,
                "event": 5,
            },
        ]

        for favorite in favorites:
            try:
                Favorite.objects.create(
                    user=User.objects.get(pk=favorite["user"]),
                    event=Event.objects.get(pk=favorite["event"]),
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully insert {self.data} > {favorite}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {favorite} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
