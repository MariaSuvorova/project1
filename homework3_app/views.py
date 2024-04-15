from django.shortcuts import render, get_object_or_404
import logging
from django.utils.timezone import now
from datetime import timedelta
from homework3_app.models import Customer, Order

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
