# Generated by Django 3.2.5 on 2021-11-03 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
