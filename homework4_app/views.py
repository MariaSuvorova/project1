from django.shortcuts import render, get_object_or_404
import logging
from django.utils.timezone import now
from datetime import timedelta
from homework4_app.models import Customer, Order, Product
from homework4_app.forms import ProductForm
from django.db import models
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Посещение страницы {__name__}: index')
    return render(request, 'homework3_app/index.html')


def about(request):
    logger.info(f'Посещение страницы {__name__}: about')
    return render(request, 'homework3_app/about.html')


def customer_orders(request, customer_id):
    logger.info(f'Запрос {__name__}: customer_orders')
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).all()
    context = {'customer': customer, 'orders': orders}
    return render(request, 'homework3_app/customer_orders.html', context)


def products_in_order(request, customer_id, order_id):
    logger.info(f'Запрос {__name__}: products_in_order')
    customer = get_object_or_404(Customer, pk=customer_id)
    order = get_object_or_404(Order, pk=order_id)
    products = set([product for product in order.products.all()])
    context = {'customer': customer, 'order': order, 'products': products}
    return render(request, 'homework3_app/products_in_order.html', context)


def products_in_orders_days_filter(request, customer_id, days):
    logger.info(f'Запрос {__name__}: products_in_orders_days_filter')
    if days in (7, 30, 365):
        day_filter = {'7': [], '30': [], '365': []}
    else:
        day_filter = {f'{days}': []}
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    for key in day_filter:
        orders = Order.objects.filter(customer=customer)
        products_list = set([product for order in orders
                             if order.creation_date >= now() - timedelta(int(key))
                             for product in order.products.all()])
        day_filter[key].extend(list(products_list))
    context['day_filter'] = day_filter
    return render(request, 'homework3_app/products_in_order_day_filter.html',
                  context)


def checker(value, model: models, field: str) -> bool:
    """проверка на существование в базе"""
    return model.objects.filter(**dict({field: value})).first() is not None


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            if checker(title, Product, 'title'):
                return HttpResponse(f'Товар "{title}" существует в БД.')
            product = Product(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                place_date=now(),
            )
            product.save()
            logger.info(f'{product} добавлен в базу')
    else:
        form = ProductForm()
    context = {'form': form, 'title': 'Создание нового товара'}
    return render(request, 'homework4_app/product_create.html', context)


def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
    form = ProductForm(instance=product)
    context = {'product': product, 'form': form, 'title': 'Обновление данных товара'}
    return render(request, 'homework4_app/product_update.html', context)
