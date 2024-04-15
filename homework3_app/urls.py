from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    path('customer/<int:customer_id>/', views.customer_orders,
         name='customer_orders'),

    path('customer/<int:customer_id>/orders/<int:order_id>/',
         views.products_in_order,
         name='products_in_order'),

    path('customer/<int:customer_id>/days/<int:days>/',
         views.products_in_orders_days_filter,
         name='products_in_orders_days_filter'),
]
