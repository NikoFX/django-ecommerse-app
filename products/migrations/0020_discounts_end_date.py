# Generated by Django 3.1.5 on 2021-03-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_discounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='discounts',
            name='end_date',
            field=models.DateField(null=True, verbose_name='Bitmə tarixi'),
        ),
    ]