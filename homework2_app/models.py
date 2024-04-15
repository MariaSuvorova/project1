from django.db import models
from django.core.validators import RegexValidator


# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
class Customer(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField()
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phoneRegex], max_length=20,
                                    unique=True)
    adress = models.TextField()
    registration_date = models.DateTimeField()

    def __str__(self):
        return f'Customer username: {self.username}, email: {self.email}, \
                phone_number: {self.phone_number}, adress: {self.adress}, \
                registration_date: {self.registration_date} '


# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
class Product(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    place_date = models.DateTimeField()

    def __str__(self):
        return f'Product title: {self.title}, desc: {self.description}, \
                price: {self.price}'


# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField()

    def __str__(self):
        return f'Order by: {self.customer.username}, products: {self.products.all()}, total: {self.total}'
