# Generated by Django 3.1.5 on 2021-10-06 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_remove_products_price_old'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Rəng')),
            ],
            options={
                'verbose_name': 'Məhsulun rəngi',
                'verbose_name_plural': 'Məhsulun rəngi',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='color_s',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.colors'),
        ),
    ]
