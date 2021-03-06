# Generated by Django 2.2.6 on 2019-11-22 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('logo', models.ImageField(blank=True, default='default', upload_to='Others')),
                ('mobile', models.CharField(max_length=12)),
                ('address', models.TextField(max_length=70)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('holiday', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('about', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=30)),
                ('is_delivaryAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('type', models.CharField(choices=[('P', 'Percentage'), ('F', 'Flat')], default='P', max_length=1)),
                ('amount', models.FloatField()),
                ('expire_date', models.DateTimeField()),
                ('number_of_coupon', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phn', models.CharField(db_index=True, max_length=11, unique=True)),
                ('location', models.TextField(max_length=50)),
                ('image', models.ImageField(blank=True, default='default', upload_to='pro_pics')),
                ('rating', models.IntegerField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('area_id', models.ForeignKey(on_delete=None, to='restaurant.Area')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('phone', models.CharField(db_index=True, max_length=11, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('sallary', models.FloatField()),
                ('address', models.TextField(max_length=70)),
                ('image', models.ImageField(blank=True, default='default', upload_to='pro_pics')),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('image_small', models.ImageField(blank=True, default='default', upload_to='others')),
                ('image_cover', models.ImageField(blank=True, default='default', upload_to='others')),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('description', models.TextField(max_length=200)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(blank=True, default='default', upload_to='gallary')),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=200)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('rating', models.IntegerField()),
                ('image', models.ImageField(blank=True, default='default', upload_to='menu')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Food_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivary_address', models.TextField(max_length=70)),
                ('note', models.TextField(max_length=100)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('coupon_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Coupon')),
                ('customer_id', models.ForeignKey(on_delete=None, to='restaurant.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Position_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=60)),
                ('person', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('method_id', models.ForeignKey(on_delete=None, to='restaurant.Payment_Method')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Ordered_food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('food_id', models.ForeignKey(on_delete=None, to='restaurant.Menu')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_status_id',
            field=models.ForeignKey(on_delete=None, to='restaurant.Order_Status'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('qty', models.FloatField()),
                ('cost', models.FloatField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('bought_by', models.ForeignKey(on_delete=None, to='restaurant.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=None, to='restaurant.Position_List'),
        ),
    ]
