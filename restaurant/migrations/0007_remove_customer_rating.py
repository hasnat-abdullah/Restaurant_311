# Generated by Django 2.2.6 on 2019-12-13 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20191207_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='rating',
        ),
    ]