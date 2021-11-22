from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emailAddress = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    answer = RichTextField(null=True, blank=True)
    NOT_ANSWER = 'NOT ANSWER'
    ANSWERED = 'ANSWERED'
    ANSWER_STATUS = [
        (NOT_ANSWER, 'NOT ANSWER'),
        (ANSWERED, 'ANSWERED'),
    ]
    status = models.CharField(max_length=30, choices=ANSWER_STATUS, default='NOT ANSWER')

    def __str__(self):
        return self.subject

