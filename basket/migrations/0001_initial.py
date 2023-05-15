# Generated by Django 3.1.5 on 2022-08-08 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie_id', models.CharField(max_length=100)),
                ('product_id', models.IntegerField()),
                ('name', models.CharField(max_length=50, verbose_name='Adı')),
                ('size', models.CharField(max_length=10, verbose_name='Ölçüsü')),
                ('image', models.ImageField(default=None, upload_to='static/product_images/', verbose_name='Şəkil')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Qiymət AZN')),
                ('count', models.IntegerField(default=0, verbose_name='Sayı')),
                ('color_purple', models.BooleanField(default=False, verbose_name='Bənövşəyi')),
                ('color_green', models.BooleanField(default=False, verbose_name='Yaşıl')),
                ('color_yellow', models.BooleanField(default=False, verbose_name='Sarı')),
                ('color_blue', models.BooleanField(default=False, verbose_name='Mavi')),
                ('color_black', models.BooleanField(default=False, verbose_name='Qara')),
                ('color_grey', models.BooleanField(default=False, verbose_name='Boz')),
                ('color_red', models.BooleanField(default=False, verbose_name='Qırmızı')),
                ('color_pink', models.BooleanField(default=False, verbose_name='Çəhrayı')),
                ('color_orange', models.BooleanField(default=False, verbose_name='Narıncı')),
                ('color_mix', models.BooleanField(default=False, verbose_name='Qarışıq')),
            ],
        ),
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(default=None, max_length=50, null=True, verbose_name='Kupon kodu')),
                ('discount', models.IntegerField(default=0, verbose_name='Endirim faizi')),
            ],
            options={
                'verbose_name': 'Kuponlar',
                'verbose_name_plural': 'Kuponlar',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Sifarişçi')),
                ('phone', models.CharField(max_length=50, null=True, verbose_name='Tel')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='Ünvan')),
                ('product', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Məhsullar')),
                ('status', models.BooleanField(default=False, verbose_name='Yerinə yetirildi')),
                ('created_date', models.DateField(auto_now_add=True, null=True, verbose_name='Sifariş tarixi')),
                ('coupon_code', models.CharField(default=None, max_length=50, null=True, verbose_name='Kupon kodu')),
                ('discount', models.IntegerField(default=0, verbose_name='Endirim')),
            ],
            options={
                'verbose_name': 'Sifarişlər',
                'verbose_name_plural': 'Sifarişlər',
            },
        ),
        migrations.CreateModel(
            name='Coupon_holders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie_id', models.CharField(max_length=100)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.coupons')),
            ],
        ),
    ]
