# Generated by Django 2.2.6 on 2019-11-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, default='default', upload_to='event_pic'),
        ),
    ]