import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from recipes.models import Tag

DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            with open(
                'data/tags.csv', 'r',
                encoding='UTF-8'
            ) as tags:
                for row in csv.reader(tags):
                    if len(row) == 3:
                        _, created = Tag.objects.get_or_create(
                            name=row[0], color=row[1], slug=row[2],
                        )
            self.stdout.write(
                self.style.SUCCESS(u'Импорт recipes_tag.csv завершён!'))
        except FileNotFoundError:
            raise CommandError('Добавьте файл tags в директорию data')
