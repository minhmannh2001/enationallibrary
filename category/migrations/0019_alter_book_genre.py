# Generated by Django 3.2.5 on 2022-01-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0018_auto_20211230_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Chính trị pháp luật', 'Chính trị pháp luật'), ('Khoa học công nghệ - Kinh tế', 'Khoa học công nghệ - Kinh tế'), ('Văn học nghệ thuật', 'Văn học nghệ thuật'), ('Văn hóa xã hội - Lịch sử', 'Văn hóa xã hội - Lịch sử'), ('Giáo dục', 'Giáo dục'), ('Tâm lý', 'Tâm lý'), ('Truyện, tiểu thuyết', 'Truyện, tiểu thuyết'), ('Tâm linh, tôn giáo', 'Tâm linh, tôn giáo'), ('Sách thiếu nhi', 'Sách thiếu nhi'), ('Truyện tranh', 'Truyện tranh')], max_length=50, verbose_name='Thể loại'),
        ),
    ]