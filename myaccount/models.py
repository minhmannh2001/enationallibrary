from django.db import models
from category.models import Book


class MemberCard(models.Model):
    NOT_EXTENSION = 'NE'
    MONTHLY_BASIC = 'MB'
    ANNUAL_BASIC = 'AB'
    MONTHLY_VIP = 'MV'
    ANNUAL_VIP = 'AV'
    servicesPlanChoices = [
        (NOT_EXTENSION, 'Not extension'),
        (MONTHLY_BASIC, 'Monthly Basic'),
        (ANNUAL_BASIC, 'Annual Basic'),
        (MONTHLY_VIP, 'Monthly VIP'),
        (ANNUAL_VIP, 'Annual VIP')
    ]
    servicePlan = models.CharField(max_length=30, choices=servicesPlanChoices)
    numOfFault = models.IntegerField()
    maxNbOfBooksToBorrow = models.IntegerField()
    nbOfBooksBeingBorrowed = models.IntegerField()
    booksBeingBorrowed = models.ManyToManyField(Book)
    registerDate = models.DateTimeField(null=True)


class User(models.Model):
    firstName = models.CharField(max_length=30, null=True, blank=True)
    lastName = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dateOfBirth = models.DateField(null=True, blank=True)
    emailAddress = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    identificationCard = models.CharField(max_length=40, null=True, blank=True)
    phoneNumber = models.CharField(max_length=10, null=True, blank=True)
    memberCard = models.OneToOneField(MemberCard, on_delete=models.CASCADE, null=True, blank=True)



