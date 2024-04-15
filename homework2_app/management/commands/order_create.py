<<<<<<< HEAD
from decimal import Decimal
from django.utils.timezone import now
from django.core.management.base import BaseCommand
from django.db import models
from homework2_app.models import Product, Customer, Order

# python manage.py order_create 6 4 5 1


def checker(value, model: models, field: str) -> bool:
    """проверка на существование в базе"""
    return model.objects.filter(**dict({field: value})).first() is not None


class Command(BaseCommand):
    help = f'Order creation with using customer.id and several product.id'

    def add_arguments(self, parser):
        parser.add_argument('customer_id', type=int, help='id клиента')
        parser.add_argument('product_id_list', type=int, nargs='*',
                            help='id товаров')

    def handle(self, *args, **options):
        customer_id = options.get('customer_id')
        product_id_list = options.get('product_id_list')

        if not checker(customer_id, Customer, 'pk'):
            return self.stdout.write(f'customer_id "{customer_id}" в БД не существует.')
        for product_id in product_id_list:
            if not checker(product_id, Product, 'pk'):
                return self.stdout.write(f'product_id "{product_id}" в БД не существует.')

        order = Order(
            customer=Customer.objects.filter(pk=customer_id).first(),
            total=0,
            creation_date=now(),
        )
        order.save()
        for id in product_id_list:
            product_to_order = Product.objects.filter(pk=id).first()
            order.products.add(product_to_order)
        order.total = sum([Decimal(i.price) for i in order.products.all()])
        order.save()

        self.stdout.write(f'{order}')
=======
from decimal import Decimal
from django.utils.timezone import now
from django.core.management.base import BaseCommand
from django.db import models
from homework2_app.models import Product, Customer, Order

# python manage.py order_create 6 4 5 1


def checker(value, model: models, field: str) -> bool:
    """проверка на существование в базе"""
    return model.objects.filter(**dict({field: value})).first() is not None


class Command(BaseCommand):
    help = f'Order creation with using customer.id and several product.id'

    def add_arguments(self, parser):
        parser.add_argument('customer_id', type=int, help='id клиента')
        parser.add_argument('product_id_list', type=int, nargs='*',
                            help='id товаров')

    def handle(self, *args, **options):
        customer_id = options.get('customer_id')
        product_id_list = options.get('product_id_list')

        if not checker(customer_id, Customer, 'pk'):
            return self.stdout.write(f'customer_id "{customer_id}" в БД не существует.')
        for product_id in product_id_list:
            if not checker(product_id, Product, 'pk'):
                return self.stdout.write(f'product_id "{product_id}" в БД не существует.')

        order = Order(
            customer=Customer.objects.filter(pk=customer_id).first(),
            total=0,
            creation_date=now(),
        )
        order.save()
        for id in product_id_list:
            product_to_order = Product.objects.filter(pk=id).first()
            order.products.add(product_to_order)
        order.total = sum([Decimal(i.price) for i in order.products.all()])
        order.save()

        self.stdout.write(f'{order}')
>>>>>>> 637cff90a8d8993df125dd367fc6c9db2e3da962
        