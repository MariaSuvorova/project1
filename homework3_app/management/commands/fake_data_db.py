from decimal import Decimal
from django.core.management.base import BaseCommand
from faker import Faker
from homework3_app.models import Customer, Product, Order
from random import choice, randint, uniform

# python manage.py fake_data_db 10 20 15
# python manage.py fake_data_db 10 5 20

class Command(BaseCommand):
    help = "Generate fake Customers, Products, Orders."

    def add_arguments(self, parser):
        parser.add_argument('customers_qty', type=int,
                            help="Customer's quantity")
        parser.add_argument('products_qty', type=int,
                            help="Product's quantity")
        parser.add_argument('orders_qty', type=int, help="Order's quantity")

    def handle(self, *args, **options):
        customers_qty = options.get('customers_qty')
        products_qty = options.get('products_qty')
        orders_qty = options.get('orders_qty')
        fake = Faker()
        for i in range(1, customers_qty + 1):
            customer = Customer(username=f'Name{i}', email=f'mail{i}@mail.ru',
                                phone_number=f"+7{''.join([str(randint(0, 9)) for _ in range(10)])}",
                                adress=f'adress{i}',
                                registration_date=fake.date_time_between(start_date='-2y', end_date='now')
                                )
            customer.save()
        for j in range(1, products_qty + 1):
            product = Product(
                title=f'Title{j}',
                description=f'description{j}',
                price=round(uniform(1, 10000), 2),
                quantity=randint(1, 100),
                place_date=fake.date_time_between(start_date='-2y', end_date='now')
            )
            product.save()
        for i in range(1, orders_qty + 1):
            customerBD = Customer.objects.all()
            productBD = Product.objects.all()

            order = Order(
                customer=choice(customerBD),
                total=0,
                creation_date=fake.date_time_between(
                    start_date=customer.registration_date,
                    end_date='now'
                    )
                )
            order.save()
            product_in_order = (choice(productBD) for _ in range(randint(1, 7)))
            order.products.set(product_in_order)
            order.total = sum([Decimal(i.price) for i in order.products.all()])
            order.save()

        self.stdout.write(f'БД заполнена: \n клиенты: {customers_qty}, \n товары: {products_qty}, \n заказы: {orders_qty}')
