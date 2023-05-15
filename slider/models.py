from django.db import models

# Create your models here.

class Slider(models.Model):
    blog = models.ForeignKey('blogs.Blogs', verbose_name='Blog', on_delete=models.CASCADE)


    def __str__(self):
        return self.blog.headline
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-id']