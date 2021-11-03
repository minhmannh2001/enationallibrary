# Generated by Django 3.2.5 on 2021-11-03 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicePlan', models.CharField(choices=[('NE', 'Not extension'), ('MB', 'Monthly Basic'), ('AB', 'Annual Basic'), ('MV', 'Monthly VIP'), ('AV', 'Annual VIP')], max_length=30)),
                ('numOfFault', models.IntegerField()),
                ('maxNumOfBorrowedBooks', models.IntegerField()),
                ('numOfBorrowedBooks', models.IntegerField()),
                ('registerDate', models.DateTimeField(null=True)),
                ('borrowedBooks', models.ManyToManyField(to='category.Book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=30, null=True)),
                ('lastName', models.CharField(blank=True, max_length=30, null=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('emailAddress', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('identificationCard', models.CharField(blank=True, max_length=40, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('memberCard', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myaccount.membercard')),
            ],
        ),
    ]