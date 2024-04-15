from django.forms import ModelForm, Textarea
from homework4_app.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'quantity',
            'image',
        ]
        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': f'Описание товара..'})
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'quantity': 'Количество',
            'image': 'Изображение',
        }