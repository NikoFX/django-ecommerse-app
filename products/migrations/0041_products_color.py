# Generated by Django 3.1.5 on 2021-10-06 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_remove_products_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='color',
            field=models.CharField(choices=[('Standart', 'Standart'), ('Rengli', 'Rəngli')], default='Standart', help_text='Əgər məhsulun rəngləri varsa RƏNGLİ seç və aşağıdan rəngləri seç. Əksi halda standart seç', max_length=15, verbose_name='Rəng tipi'),
        ),
    ]