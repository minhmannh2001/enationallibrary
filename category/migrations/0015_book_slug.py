# Generated by Django 3.2.5 on 2021-12-23 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0014_book_israre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.CharField(default='sach-slug', max_length=255),
            preserve_default=False,
        ),
    ]
