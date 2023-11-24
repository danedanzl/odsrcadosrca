from django.core.management.base import BaseCommand, CommandError
from django.urls import reverse

import segno

from naloge.tasklist import task_list

# XXX: should be in settings.py or something
ROOT_URL = "https://odsrcadosrca.rodsivegavolka.si"

class Command(BaseCommand):
    help = "Generate QR code images in current dir"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for t in task_list:
            url = ROOT_URL + reverse(t.__name__)
            qr = segno.make_qr(url)
            qr.save(f"qr/{t.__name__}.png", scale=5, border=2)
            self.stdout.write(
                self.style.SUCCESS(reverse(t.__name__))
            )
