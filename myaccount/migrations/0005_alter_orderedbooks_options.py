# Generated by Django 3.2.5 on 2021-12-13 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0004_orderedbooks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderedbooks',
            options={'verbose_name': 'Danh sách sách đã mượn', 'verbose_name_plural': 'Quản lý danh sách sách đã mượn'},
        ),
    ]
