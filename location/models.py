from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from category.models import Book, Publisher, Author


class Event(models.Model):
    eventName = models.CharField(max_length=255, verbose_name='Tên sự kiện', unique=True)
    startDate = models.DateTimeField(verbose_name='Ngày bắt đầu')
    endDate = models.DateTimeField(verbose_name='Ngày kết thúc')
    content = models.TextField(verbose_name='Nội dung khuyến mãi')
    banner = models.ImageField(verbose_name='Banner sự kiện')
    image = models.ImageField(verbose_name='Ảnh sự kiện', default='image.jpg')
    slug = models.SlugField(max_length=255, null=True, blank=True)
    discountFactor = models.IntegerField(
        default=50,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ],
        verbose_name='Tỷ lệ giảm giá(%)'
    )

    class Meta:
        verbose_name = 'Sự kiện'
        verbose_name_plural = 'Quản lý sự kiện'
