# Generated by Django 3.2.5 on 2021-11-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_alter_contact_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='firstName',
            field=models.CharField(max_length=50, verbose_name='Họ'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='lastName',
            field=models.CharField(max_length=50, verbose_name='Tên'),
        ),
    ]
