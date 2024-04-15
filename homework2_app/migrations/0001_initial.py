
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('adress', models.TextField()),
                ('registration_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('place_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creation_date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework2_app.customer')),
                ('products', models.ManyToManyField(to='homework2_app.product')),
            ],
        ),
    ]
