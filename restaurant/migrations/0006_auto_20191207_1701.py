# Generated by Django 2.2.6 on 2019-12-07 11:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_cart',
            name='customer_id',
            field=models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
