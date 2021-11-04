from django.db import models
from login.models import Author, Publisher


class Book(models.Model):
    title = models.CharField(max_length=100)
    EBOOK = 'EB'
    BOOK = 'NB'
    bookType = [
        (EBOOK, 'EBOOK'),
        (BOOK, 'BOOK')
    ]
    type = models.CharField(max_length=10, choices=bookType)
    author = models.ManyToManyField(Author)
    publisher = models.ManyToManyField(Publisher)
    language = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    summary = models.TextField()
    image = models.ImageField()
    quantity = models.IntegerField()
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
    genre = models.CharField(max_length=20, choices=bookGenre)
    rating = models.IntegerField()
    # comments

    def __str__(self):
        return self.title


class Magazine(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    pdfFile = models.FileField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class New(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    createdAt = models.DateTimeField()
    author = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)
    description = models.TextField()
    creator = models.TextField()

    def __str__(self):
        return self.title
