from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name