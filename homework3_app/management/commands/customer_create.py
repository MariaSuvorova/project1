from django.utils.timezone import now
from django.core.management.base import BaseCommand
from django.db import models
from homework2_app.models import Customer

# python manage.py customer_create Jhon sss@test.com +79898098 adress56


def checker(value, model: models, field: str) -> bool:
    """проверка на существование в базе"""
    return model.objects.filter(**dict({field: value})).first() is not None

class Command(BaseCommand):
    help = 'Customer creation'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='имя клиента')
        parser.add_argument('email', type=str, 
                            help='электронная почта клиента')
        parser.add_argument('phone_number', type=str,
                            help='номер телефона клиента')
        parser.add_argument('adress', type=str, help='адрес клиента')

    def handle(self, *args, **options):
        username = options.get('username')
        email = options.get('email')
        phone_number = options.get('phone_number')
        adress = options.get('adress')

        if checker(username, Customer, 'username'):
            return self.stdout.write(f'username: "{username}" \
                                     существует в БД.')
        if checker(email, Customer, 'email'):
            return self.stdout.write(f'email: "{email}" существует в БД.')
        if checker(phone_number, Customer, 'phone_number'):
            return self.stdout.write(f'phone_number: "{phone_number}" \
                                     существует в БД.')

        customer = Customer(
            username=username,
            email=email,
            phone_number=phone_number,
            adress=adress,
            registration_date=now(),
        )
        customer.save()

        self.stdout.write(f'{customer}')
        