from django.db import models
from products.models import Products
from django.contrib import admin
# Create your models here.

class Basket(models.Model):
    cookie_id = models.CharField(max_length=100)
    product_id = models.IntegerField()
    name = models.CharField('Name', max_length=50)
    size = models.CharField('Size', max_length=10)
    image = models.ImageField('Image', upload_to='static/product_images/', default=None)
    price = models.DecimalField(verbose_name='Price AZN', null=False, default=0.00, max_digits=6, decimal_places=2)
    count = models.IntegerField('Count', default=0,)
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

class Orders(models.Model):
    name = models.CharField('Customer', max_length=100)
    phone = models.CharField('Tel. No', max_length=50, null=True)
    address = models.CharField('Address', max_length=50, null=True)
    product = models.TextField('Products', max_length=1000, null=True, blank=True)
    status = models.BooleanField('Have done', default=False)
    created_date = models.DateField('Order date', auto_now_add=True, null=True)
    coupon_code = models.CharField('Coupon code', max_length=50, null=True, default=None)
    discount = models.IntegerField('Discount', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'

class Coupons(models.Model):
    coupon_code = models.CharField('Coupon code', max_length=50, null=True, default=None)
    discount = models.IntegerField('Discount precent', default=0)
    including = models.IntegerField('Min. order price by AZN', default=0)

    def __str__(self):
        return self.coupon_code

    class Meta:
        verbose_name = 'Coupons'
        verbose_name_plural = 'Coupons'

class Coupon_holders(models.Model):
    cookie_id = models.CharField(max_length=100)
    coupon = models.CharField('Coupon code', max_length=50, null=True, default=None)

class Min_order(models.Model):
    name = models.CharField('Delivery free', max_length=50, default='Edit')
    delivery_price = models.IntegerField('Delivery fee by AZN', default=0)
    price = models.IntegerField('Min. order for free delivery by AZN', default=0)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Delivery'
