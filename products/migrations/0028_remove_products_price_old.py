# Generated by Django 3.1.5 on 2021-10-06 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_merge_20210612_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price_old',
        ),
    ]