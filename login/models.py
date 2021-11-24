from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tên tác giả')
    description = models.TextField(verbose_name='Giới thiệu về tác giả')
    image = models.ImageField(null=True, verbose_name='Hình ảnh tác giả')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tác giả'
        verbose_name_plural = 'Quản lý tác giả'


class Publisher(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tên nhà xuất bản')
    description = models.TextField(verbose_name='Giới thiệu về nhà xuất bản')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'nhà xuất bản'
        verbose_name_plural = 'Quản lý nhà xuất bản'