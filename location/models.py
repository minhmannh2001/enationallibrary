from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from category.models import Book, Publisher, Author


class Event(models.Model):
    eventName = models.CharField(max_length=255)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    content = models.TextField()
    banner = models.ImageField()
    discountFactor = models.IntegerField(
        default=50,
        validators=[
            MinValueValidator(100),
            MaxValueValidator(1)
        ]
    )
    appliedBooks = models.ManyToManyField(Book)
    appliedAuthors = models.ManyToManyField(Author)
    appliedPublisher = models.ManyToManyField(Publisher)
