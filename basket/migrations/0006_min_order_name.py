# Generated by Django 3.1.5 on 2022-08-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_auto_20220809_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='min_order',
            name='name',
            field=models.CharField(default='Minimum sifariş', max_length=50, verbose_name='Minimum sifariş'),
        ),
    ]
