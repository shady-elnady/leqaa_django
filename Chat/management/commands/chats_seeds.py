# from django.core.management.base import BaseCommand
# from django.core.management import call_command


# class Command(BaseCommand):
#     help = "Creates initial Chat Load Data"

#     def handle(self, *args, **options):
#         load_data = [
#             "languages.json",
#             "locales.json",
#         ]
#         for data in load_data:
#             try:
#                 call_command("loaddata", data)
#                 self.stdout.write(self.style.SUCCESS(f"Successfully {data} Load Data"))
#             except Exception as e:
#                 self.stdout.write(
#                     self.style.ERROR(
#                         f"Load Data Failed from {data} , \n \t Error is: \t \t{e}"
#                     )
#                 )

#         self.stdout.write(self.style.SUCCESS("Successfully initial Chat Load Data"))
