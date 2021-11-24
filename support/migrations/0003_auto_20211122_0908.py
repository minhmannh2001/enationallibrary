# Generated by Django 3.2.5 on 2021-11-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_auto_20211122_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[(0, 'NOT ANSWER'), (1, 'ANSWERED')], default='NOT ANSWER', max_length=30),
        ),
    ]