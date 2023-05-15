# Generated by Django 3.1.5 on 2021-10-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_products_color_mix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.CharField(choices=[('Standart', 'Qarisiq')], max_length=15, verbose_name='Rəng tipi'),
        ),
    ]