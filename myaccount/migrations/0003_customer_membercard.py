# Generated by Django 3.2.5 on 2021-12-12 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0011_book_createdat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myaccount', '0002_auto_20211212_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicePlan', models.CharField(choices=[('NE', 'Chưa đăng ký'), ('MB', 'Thẻ tháng thường'), ('AB', 'Thẻ năm thường'), ('MV', 'Thẻ tháng VIP'), ('AV', 'Thẻ năm VIP')], max_length=30, verbose_name='Gói dịch vụ')),
                ('numOfFault', models.IntegerField(verbose_name='Số lỗi đã vi phạm')),
                ('maxNbOfBooksToBorrow', models.IntegerField(verbose_name='Số lượng sách mượn tối đa')),
                ('nbOfBooksBeingBorrowed', models.IntegerField(verbose_name='Số lượng sách đang mượn')),
                ('registerDate', models.DateTimeField(null=True, verbose_name='Ngày đăng ký')),
                ('booksBeingBorrowed', models.ManyToManyField(to='category.Book', verbose_name='Những cuốn sách đang mượn')),
            ],
            options={
                'verbose_name': 'thẻ thành viên',
                'verbose_name_plural': 'Quản lý thẻ thành viên',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(blank=True, max_length=30, null=True, verbose_name='Họ')),
                ('firstName', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tên')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Tên đăng nhập')),
                ('dateOfBirth', models.DateField(blank=True, null=True, verbose_name='Ngày sinh')),
                ('emailAddress', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Địa chỉ email')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Địa chỉ nhà')),
                ('identificationCard', models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='Số CMND')),
                ('phoneNumber', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Số điện thoại')),
                ('memberCard', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myaccount.membercard', verbose_name='Thẻ đã đăng ký')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'người dùng',
                'verbose_name_plural': 'Quản lý người dùng',
            },
        ),
    ]
