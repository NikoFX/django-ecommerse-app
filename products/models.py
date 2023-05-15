from django.db import models
from ckeditor.fields import RichTextField
import random

# Create your models here.
class Products(models.Model):


    category_choices = [
        ('interdental', 'Interdental Brushes'),
        ('toothpicks', 'Toothpicks'),
        ('dental_floss', 'Dental floss'),
        ('brushers', 'Toothbrushes'),
        ('accesories', 'Accesories')
    ]
    colortype_choices = [('Standart', 'Standart'), ('Qarisiq', 'Qarisiq')]
    company_choices = [('all', 'All'), ('tepe', 'TePe'), ('bilimplant', 'Bilimplant'),  ('miradent', 'Miradent'), ('aquapick', 'Aquapick')]

    image1 = models.ImageField('Şəkil 1', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    image2 = models.ImageField('Şəkil 2', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    image3 = models.ImageField('Şəkil 3', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    image4 = models.ImageField('Şəkil 4', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    image5 = models.ImageField('Şəkil 5', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    name = models.CharField('Name', max_length=100)
    color = models.CharField(choices=colortype_choices, default='Standart', verbose_name='Color type',
                                    max_length=15,
                                    help_text='Əgər məhsulun rəngləri varsa RƏNGLİ seç və aşağıdan rəngləri seç. Əksi halda standart seç')
    color_purple = models.BooleanField(default=False, verbose_name='Fiolet')
    color_green = models.BooleanField(default=False, verbose_name='Green')
    color_yellow = models.BooleanField(default=False, verbose_name='Yellow')
    color_blue = models.BooleanField(default=False, verbose_name='Blue')
    color_black = models.BooleanField(default=False, verbose_name='Black')
    color_grey = models.BooleanField(default=False, verbose_name='Silver')
    color_red = models.BooleanField(default=False, verbose_name='Red')
    color_pink = models.BooleanField(default=False, verbose_name='Pink')
    color_orange = models.BooleanField(default=False, verbose_name='Orange')
    color_mix = models.BooleanField(default=False, verbose_name='Mix')
    size = models.CharField('Size', max_length=50)
    detail_mini = models.CharField('Short description', max_length=180)
    detail_main = models.TextField('Base description', max_length=800)
    #detail_main = RichTextField('Əsas məlumat', max_length=500)
    category = models.CharField(choices=category_choices, verbose_name='Category', max_length=30)
    price = models.DecimalField(verbose_name='Price AZN', null=False, default=0.00, max_digits=6, decimal_places=2)
    price_discount = models.DecimalField(verbose_name='Discount', null=False, default=0.00, max_digits=6, decimal_places=2, help_text='Yoxdursa boş burax')
    discount = models.BooleanField(default=False, verbose_name='Discount')
    discount_precent = models.IntegerField('Precent', null=True, default=0)
    status = models.BooleanField(default=True, verbose_name='Aviable for everyone')
    company = models.CharField(choices=company_choices, verbose_name='Company', help_text='Hansı saytda görünməsini istəyirsən?', default='all', null=True, max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Discounts(models.Model):
    name = models.CharField('Name', max_length=20)
    precent = models.IntegerField('Discount precent %')
    end_date = models.DateField('Ending date', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'
        ordering = ['id']

class Popular(models.Model):
    name = models.ForeignKey('products.Products', verbose_name='Best selling products', on_delete=models.PROTECT)

    def __str__(self):
        return self.name.name

    class Meta:
        verbose_name = 'Best selling products'
        verbose_name_plural = 'Best selling products'