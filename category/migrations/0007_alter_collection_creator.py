# Generated by Django 3.2.5 on 2021-11-22 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_alter_book_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='creator',
            field=models.CharField(max_length=255),
        ),
    ]