# Generated by Django 2.2.6 on 2019-12-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20191201_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=None, to='restaurant.Customer')),
                ('food_id', models.ForeignKey(on_delete=None, to='restaurant.Menu')),
            ],
        ),
    ]
