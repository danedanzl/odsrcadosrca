from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
    help = "Initialize"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            os.stat("qr")
        except FileNotFoundError:
            os.mkdir("qr")
            self.stdout.write(
                self.style.SUCCESS("'qr/' created")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("'qr/' already exists")
            )


