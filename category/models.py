from django.db import models
from login.models import Author, Publisher
from ckeditor.fields import RichTextField


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Tiêu đề')
    EBOOK = 'EB'
    BOOK = 'NB'
    bookType = [
        (EBOOK, 'Sách điện tử'),
        (BOOK, 'Sách giấy')
    ]
    type = models.CharField(max_length=10, choices=bookType, verbose_name='Loại sách')
    author = models.ManyToManyField(Author, verbose_name='Tác giả')
    publisher = models.ManyToManyField(Publisher, verbose_name='Nhà xuất bản')
    language = models.CharField(max_length=20, verbose_name='Ngôn ngữ')
    description = models.CharField(max_length=255, verbose_name='Mô tả')
    summary = RichTextField(verbose_name='Tóm tắt nội dung')
    image = models.ImageField(verbose_name='Ảnh bìa')
    quantity = models.IntegerField(verbose_name='Số lượng')
    beingBorrowedQuantity = models.IntegerField(default=0, verbose_name='Số lượng đã mượn')
    Chinhtriphapluat = 'CTPL'
    KhoahocCongngheKinhte = 'KHCNKT'
    Vanhocnghethuat = 'VHNT'
    VanhoaxahoiLichsu = 'VHXHLS'
    Truyentieuthuyet = 'TTT'
    TamlinhTongiao = 'TLTG'
    Sachthieunhi = 'STN'
    Truyentranh = 'TT'
    Giaoduc = 'GD'
    Tamly = 'TL'
    bookGenre = [
        (Chinhtriphapluat, 'Chính trị pháp luật'),
        (KhoahocCongngheKinhte, 'Khoa học công nghệ - Kinh tế'),
        (Vanhocnghethuat, 'Văn học nghệ thuật'),
        (VanhoaxahoiLichsu, 'Văn hóa xã hội - Lịch sử'),
        (Giaoduc, 'Giáo dục'),
        (Tamly, 'Tâm lý'),
        (Truyentieuthuyet, 'Truyện, tiểu thuyết'),
        (TamlinhTongiao, 'Tâm linh, tôn giáo'),
        (Sachthieunhi, 'Sách thiếu nhi'),
        (Truyentranh, 'Truyện tranh'),
    ]
    genre = models.CharField(max_length=20, choices=bookGenre, verbose_name='Thể loại')
    rating = models.IntegerField(verbose_name='Đánh giá')
    # comments

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'sách'
        verbose_name_plural = 'Quản lý sách'


class Magazine(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tiêu đề')
    summary = models.TextField(verbose_name='Tóm tắt nội dung')
    pdfFile = models.FileField(verbose_name='File PDF')
    image = models.ImageField(verbose_name='Ảnh bìa')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tạp chí'
        verbose_name_plural = 'Quản lý tạp chí'


class New(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tiêu đề')
    summary = models.TextField(verbose_name='Tóm tắt nội dung')
    createdAt = models.DateTimeField(verbose_name='Ngày tạo')
    author = models.CharField(max_length=50, verbose_name='Tác giả')
    image = models.ImageField(verbose_name='Hình ảnh')
    content = RichTextField(verbose_name='Nội dung bài viết')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tin tức'
        verbose_name_plural = 'Quản lý tin tức'


class Collection(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tiêu đề')
    books = models.ManyToManyField(Book, verbose_name='Bao gồm')
    description = RichTextField(verbose_name='Bản mô tả')
    creator = models.CharField(max_length=255, verbose_name='Người tạo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'bộ sưu tập'
        verbose_name_plural = 'Quản lý bộ sưu tập'
