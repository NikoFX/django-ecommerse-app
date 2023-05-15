from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blogs(models.Model):

    company_choices = [('all', 'All'), ('tepe', 'TePe'), ('bilimplant', 'Bilimplant'), ('miradent', 'Miradent')]

    headline = models.CharField('Header', max_length=100)
    image = models.ImageField('Image (main page)', upload_to='static/blog_images/', help_text='min. 1920*1080', default=None, blank=True)
    sekil2 = models.ImageField('Image (Blog)', upload_to='static/blog_images/', default=None, blank=True)
    short_blog = models.CharField('Short description', max_length=100, help_text='Lorem ipsum...', null=True)
    main_blog = RichTextField('Main blog', max_length=100000)
    created_date = models.DateField('Date')
    company = models.CharField(choices=company_choices, verbose_name='Company', help_text='Hansı saytda görünməsini istəyirsən?', default='all', null=True, max_length=15)


    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'