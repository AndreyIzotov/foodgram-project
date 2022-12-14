import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from recipes.models import Ingredient

DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    """
    Добавляем ингредиенты из файла CSV
    """
    help = 'loading ingredients from data in json or csv'

    def handle(self, *args, **options):
        try:
            with open(
                'data/ingredients.csv', 'r',
                encoding='UTF-8'
            ) as ingredients:
                for row in csv.reader(ingredients):
                    if len(row) == 2:
                        _, created = Ingredient.objects.get_or_create(
                            name=row[0], measurement_unit=row[1],
                        )
            self.stdout.write(
                self.style.SUCCESS(u'Импорт ingredients.csv завершён!'))
        except FileNotFoundError:
            raise CommandError('Добавьте файл ingredients в директорию data')
