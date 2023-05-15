from django.db import models

# Create your models here.

class Calls(models.Model):
    name = models.CharField('Customer', max_length=50)
    phone = models.CharField('Tel No', max_length=20)
    message = models.CharField('Request text', max_length=200)
    created_date = models.DateTimeField('Date', auto_now_add=True)
    status = models.BooleanField('Has been called', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer waiting for a call'
        verbose_name_plural = 'Customers waiting for a call'