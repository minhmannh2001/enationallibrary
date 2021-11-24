from django.db import models
from category.models import Book


class MemberCard(models.Model):
    NOT_EXTENSION = 'NE'  # Not extension
    MONTHLY_BASIC = 'MB'  # Monthly Basic
    ANNUAL_BASIC = 'AB'   # Annual Basic
    MONTHLY_VIP = 'MV'    # Monthly VIP
    ANNUAL_VIP = 'AV'     # Monthly VIP
    servicesPlanChoices = [
        (NOT_EXTENSION, 'Chưa đăng ký'),
        (MONTHLY_BASIC, 'Thẻ tháng thường'),
        (ANNUAL_BASIC, 'Thẻ năm thường'),
        (MONTHLY_VIP, 'Thẻ tháng VIP'),
        (ANNUAL_VIP, 'Thẻ năm VIP')
    ]
    servicePlan = models.CharField(max_length=30, choices=servicesPlanChoices, verbose_name='Gói dịch vụ')
    numOfFault = models.IntegerField(verbose_name='Số lỗi đã vi phạm')
    maxNbOfBooksToBorrow = models.IntegerField(verbose_name='Số lượng sách mượn tối đa')
    nbOfBooksBeingBorrowed = models.IntegerField(verbose_name='Số lượng sách đang mượn')
    booksBeingBorrowed = models.ManyToManyField(Book, verbose_name='Những cuốn sách đang mượn')
    registerDate = models.DateTimeField(null=True, verbose_name='Ngày đăng ký')

    def __str__(self):
        return self.servicePlan + ' mã số ' + self.id

    class Meta:
        verbose_name = 'thẻ thành viên'
        verbose_name_plural = 'Quản lý thẻ thành viên'


class User(models.Model):
    lastName = models.CharField(max_length=30, null=True, blank=True, verbose_name='Họ')
    firstName = models.CharField(max_length=30, null=True, blank=True, verbose_name='Tên')
    username = models.CharField(max_length=50, verbose_name='Tên đăng nhập', unique=True)
    password = models.CharField(max_length=50, verbose_name='Mật khẩu')
    dateOfBirth = models.DateField(null=True, blank=True, verbose_name='Ngày sinh')
    emailAddress = models.CharField(max_length=50, null=True, blank=True, verbose_name='Địa chỉ email', unique=True)
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Địa chỉ nhà')
    identificationCard = models.CharField(max_length=40, null=True, blank=True, verbose_name='Số CMND', unique=True)
    phoneNumber = models.CharField(max_length=10, null=True, blank=True, verbose_name='Số điện thoại', unique=True)
    memberCard = models.OneToOneField(MemberCard, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Thẻ đã đăng ký', unique=True)

    def __str__(self):
        return self.lastName + ' ' + self.firstName

    class Meta:
        verbose_name = 'người dùng'
        verbose_name_plural = 'Quản lý người dùng'

