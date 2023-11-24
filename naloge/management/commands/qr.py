import os
import subprocess

from django.core.management.base import BaseCommand, CommandError
from django.urls import reverse

import segno

from naloge.views import task_list

# XXX: should be in settings.py or something
ROOT_URL = "https://odsrcadosrca.rodsivegavolka.si"

class Command(BaseCommand):
    help = "Generate QR code images in current dir"

    def add_arguments(self, parser):
        pass

    def run(self, *args):
        p = subprocess.run(args)
        if p.returncode:
            print(dir(self.style))
            self.stdout.write(
                self.style.ERROR(f"Process '{' '.join(args)} failed with code {p.returncode}'"))
            return False
        return True


    def handle(self, *args, **options):
        for t in task_list:
            url = ROOT_URL + reverse(t.info_viewname)
            qr = segno.make_qr(url)
            qr.save(f"qr/qr.svg", scale=6, border=1)
            self.run("montage", # zlimaj skupi srcka in QR kodo
                    "assets/srck1.svg", "qr/qr.svg", "assets/srck2.svg",
                    "-tile", "3x1",
                    "-geometry", "+30+30",
                    "-resize", "600x",
                    "qr/out.png")
            self.run("magick", # zrenderaj url
                     "-background", "white",
                     "-fill", "black",
                     "-font", "Open-Sans-Regular",
                     "-pointsize", "50",
                     "-gravity", "center",
                     f"label:Če ti ne uspe odčitati QR kode, lahko v brskalnik vtipkaš povezavo\n{url}",
                     "qr/label.png")
            self.run("magick", # dodaj primerno paddinga okrog urlja
                     "qr/label.png",
                     "-resize", "1980x150",
                     "-gravity", "center",
                     "-extent", "1980x150",
                     "qr/label2.png")
            self.run("montage", # zlimaj srcke + QR in text
                     "qr/out.png", "qr/label2.png",
                     "-tile", "1x2",
                     "-geometry", "+0+0",
                     "-gravity", "center",
                     "qr/out2.png")
            self.run("magick", # dodaj padding in rob da je jasno kje je konce paddinga
                     "out2.png",
                     "-bordercolor", "white",
                     "-border", "100x100",
                     "-bordercolor", "teal",
                     "-border", "3x3",
                     f"qr/{t.name}.png")
            os.remove("qr/label.png")
            os.remove("qr/label2.png")
            os.remove("qr/out.png")
            os.remove("qr/out2.png")


            self.stdout.write(
                self.style.SUCCESS(url)
            )
