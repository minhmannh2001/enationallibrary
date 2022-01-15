from django.db import models
from category.models import Book
from django.contrib.auth.models import User


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
        return f'{self.servicePlan} mã số {self.id}'

    class Meta:
        verbose_name = 'thẻ thành viên'
        verbose_name_plural = 'Quản lý thẻ thành viên'


class Customer(models.Model):
    lastName = models.CharField(max_length=30, null=True, blank=True, verbose_name='Họ')
    firstName = models.CharField(max_length=30, null=True, blank=True, verbose_name='Tên')
    username = models.CharField(max_length=50, verbose_name='Tên đăng nhập', unique=True)
    user = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
    dateOfBirth = models.DateField(null=True, blank=True, verbose_name='Ngày sinh')
    gender_choice = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
        ('Không xác định', 'Không xác định'),
    ]
    gender = models.CharField(max_length=50, null=True, blank=True, verbose_name='Giới tính')
    emailAddress = models.CharField(max_length=50, null=True, blank=True, verbose_name='Địa chỉ email', unique=True)
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Địa chỉ nhà')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='Thành phố')
    identificationCard = models.CharField(max_length=40, null=True, blank=True, verbose_name='Số CMND', unique=True)
    phoneNumber = models.CharField(max_length=10, null=True, blank=True, verbose_name='Số điện thoại', unique=True)
    memberCard = models.OneToOneField(MemberCard, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Thẻ đã đăng ký', unique=True)

    def __str__(self):
        return f'{self.lastName} {self.firstName}'

    class Meta:
        verbose_name = 'người dùng'
        verbose_name_plural = 'Quản lý người dùng'


class OrderedBooks(models.Model):
    book = models.ForeignKey(Book, related_name='ordered_list', verbose_name='Sách mượn', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='customer_list', verbose_name='Người mượn', on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name='Ngày mượn')
    expired_date = models.DateTimeField(verbose_name='Ngày hết hạn mượn')
    return_date = models.DateTimeField(verbose_name='Ngày trả sách')
    normal = 'Bình thường'
    expired_5days = 'Quá hạn mức 1'
    expried_30days = 'Quá hạn mức 2'
    returned = 'Đã trả'
    order_status = [
        (normal, 'Bình thường'),
        (expired_5days, 'Quá hạn mức 1'),
        (expried_30days, 'Quá hạn mức 2'),
        (returned, 'Đã trả')
    ]
    status = models.CharField(max_length=30, choices=order_status, verbose_name='Trạng thái mượn')

    class Meta:
        verbose_name = 'Danh sách sách đã mượn'
        verbose_name_plural = 'Quản lý danh sách sách đã mượn'

    def __str__(self):
        return f'{self.book}'
