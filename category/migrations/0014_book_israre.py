# Generated by Django 3.2.5 on 2021-12-23 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0013_alter_book_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isRare',
            field=models.BooleanField(default=False, verbose_name='Sách hiếm'),
        ),
    ]
