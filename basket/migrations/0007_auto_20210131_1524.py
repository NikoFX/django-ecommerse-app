# Generated by Django 3.1.5 on 2021-01-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_orders_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Sifariş tarixi'),
        ),
    ]
