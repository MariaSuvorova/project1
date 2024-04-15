from decimal import Decimal
from django.db import models
from django.utils.timezone import now
from django.core.management.base import BaseCommand
from homework2_app.models import Product


def checker(value, model: models, field: str) -> bool:
    """проверка на существование в базе"""
    return model.objects.filter(**dict({field: value})).first() is not None


class Command(BaseCommand):
    help = f'Product creation'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='название товара')
        parser.add_argument('description', type=str, help='описание товара')
        parser.add_argument('price', type=Decimal, help='цена товара')
        parser.add_argument('quantity', type=int, help='количество товара')

    def handle(self, *args, **options):
        title = options.get('title')
        description = options.get('description')
        price = options.get('price')
        quantity = options.get('quantity')

        if checker(title, Product, 'title'):
            return self.stdout.write(f'title: "{title}" существует в БД.')
            
        product = Product(
            title=title,
            description=description,
            price=price,
            quantity=quantity,
            place_date=now(),
        )
        product.save()

        self.stdout.write(f'{product}')