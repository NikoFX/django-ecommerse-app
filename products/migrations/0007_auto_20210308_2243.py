# Generated by Django 3.1.5 on 2021-03-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210302_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(max_length=50, verbose_name='Ölçüsü'),
        ),
    ]
