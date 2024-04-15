from django.contrib import admin
from homework4_app.models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number']
    ordering = ['username']
    list_filter = ['registration_date']
    search_fields = ['username']
    search_help_text = 'Поиск по полю Имя клиента (username)'
    readonly_fields = ['username', 'phone_number', 'registration_date']
    fieldsets = [
        (
            None, 
            {
                'classes': ['wide'], 
                'fields': ['username', 'registration_date']
            },
        ),
        (
            'Данные пользователя', 
            {
                'classes': ['collapse'], 
                'fields': ['email', 'phone_number', 'adress']
            },
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'quantity', 'image']
    ordering = ['title', 'price']
    search_fields = ['title', 'description', 'price']
    search_help_text = 'Поиск по полю: Название (title), Описание (description), Цена (price)'
    readonly_fields = ['title', 'price', 'quantity', 'place_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title', 'place_date']
            },
        ),
        (
            'Данные продукта',
            {
                'classes': ['wide'],
                'fields': ['description', 'image']
            },
        ),
        (
            'Продажи',
            {
                'classes': ['collapse'], 
                'fields': ['price', 'quantity']
                },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total', 'creation_date']
    ordering = ['customer']
    list_filter = ['customer', 'products', 'creation_date']
    search_fields = ['products']
    readonly_fields = ['total', 'products', 'creation_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['creation_date']
            },
        ),
        (
            'Данные клиента',
            {
                'classes': ['wide'], 
                'fields': ['customer']
            },
        ),
        (
            'Данные заказа',
            {
                'classes': ['wide'], 
                'fields': ['products', 'total']
            },
        ),
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)