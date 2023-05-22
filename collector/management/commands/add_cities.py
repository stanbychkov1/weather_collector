import csv
import os

from django.core.management import BaseCommand

from collector import models
from weather_collector import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(
                os.path.join(settings.BASE_DIR, 'cities.csv'),
                encoding='utf-8',
        ) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                _, _ = models.City.objects.get_or_create(
                    name=row[0],
                    longitude=row[1],
                    latitude=row[2],
                    country_code=row[3])
