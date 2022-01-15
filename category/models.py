from django.db import models
from login.models import Author, Publisher
from ckeditor.fields import RichTextField


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Tiêu đề')
    EBOOK = 'Bản điện tử'
    BOOK = 'Bản giấy'
    BOTH = 'Cả hai'
    bookType = [
        (EBOOK, 'Sách điện tử'),
        (BOOK, 'Sách giấy'),
        (BOTH, 'Cả hai'),
    ]
    type = models.CharField(max_length=20, choices=bookType, verbose_name='Loại sách')
    # slug = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    isRare = models.BooleanField(default=False, verbose_name='Sách hiếm')
    createdAt = models.DateTimeField(auto_now_add=True)
    author = models.ManyToManyField(Author, verbose_name='Tác giả')
    publisher = models.ManyToManyField(Publisher, verbose_name='Nhà xuất bản')
    publishYear = models.DateField(verbose_name='Năm xuất bản')
    language = models.CharField(max_length=20, verbose_name='Ngôn ngữ')
    description = models.CharField(max_length=255, verbose_name='Mô tả')
    summary = RichTextField(verbose_name='Tóm tắt nội dung')
    image = models.ImageField(verbose_name='Ảnh bìa')
    quantity = models.IntegerField(verbose_name='Số lượng')
    beingBorrowedQuantity = models.IntegerField(default=0, verbose_name='Số lượng đã mượn')
    Chinhtriphapluat = 'Chính trị pháp luật'
    KhoahocCongngheKinhte = 'Khoa học công nghệ - Kinh tế'
    Vanhocnghethuat = 'Văn học nghệ thuật'
    VanhoaxahoiLichsu = 'Văn hóa xã hội - Lịch sử'
    Truyentieuthuyet = 'Truyện, tiểu thuyết'
    TamlinhTongiao = 'Tâm linh, tôn giáo'
    Sachthieunhi = 'Sách thiếu nhi'
    Truyentranh = 'Truyện tranh'
    Giaoduc = 'Giáo dục'
    Tamly = 'Tâm lý'
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
    genre = models.CharField(max_length=50, choices=bookGenre, verbose_name='Thể loại')
    rating = models.IntegerField(verbose_name='Đánh giá')
    # comments

    def __str__(self):
        return self.title

    def as_json(self):
        return { "image" : self.image.url,
                    "genre" : self.genre,
                    "title" :  self.title,
                    "author" : self.author.first().name,
                    "type" : self.type,
                    "summary" : self.summary,
                    "slug" : self.slug,
                    }

    class Meta:
        verbose_name = 'sách'
        verbose_name_plural = 'Quản lý sách'


class Magazine(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tiêu đề')
    summary = models.TextField(verbose_name='Tóm tắt nội dung')
    pdfFile = models.FileField(verbose_name='File PDF')
    image = models.ImageField(verbose_name='Ảnh bìa')
    magazineGenre = [
        ('Time', 'Time'),
        ('Money', 'Money'),
        ('Economist', 'Economist'),
        ('Forbes', 'Forbes'),
        ('GQ', 'GQ'),
        ('Entrepreneur', 'Entrepreneur'),
        ('TheNewYorker', 'TheNewYorker'),
        ('Elle', 'Elle'),
    ]
    genre = models.CharField(max_length=50, choices=magazineGenre, verbose_name='Thể loại')
    publishYear = models.DateField(verbose_name='Năm xuất bản')

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
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tin tức'
        verbose_name_plural = 'Quản lý tin tức'


class Review(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tiêu đề')
    summary = models.TextField(verbose_name='Tóm tắt nội dung')
    createdAt = models.DateTimeField(verbose_name='Ngày tạo')
    author = models.CharField(max_length=50, verbose_name='Tác giả')
    image = models.ImageField(verbose_name='Hình ảnh')
    content = RichTextField(verbose_name='Nội dung bài viết')
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'bài đánh giá'
        verbose_name_plural = 'Quản lý bài đánh giá'


class Collection(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tiêu đề')
    brief_sum = models.CharField(max_length=255, verbose_name='Tóm tắt ngắn gọn', default='abc')
    image = models.ImageField(verbose_name='Ảnh bìa', default='anh_bia.jpg')
    books = models.ManyToManyField(Book, verbose_name='Bao gồm')
    description = RichTextField(verbose_name='Bản mô tả')
    creator = models.CharField(max_length=255, verbose_name='Người tạo')
    creator_role = models.CharField(max_length=255, verbose_name='Chức vụ', default='Thủ thư')
    creator_image = models.ImageField(verbose_name='Ảnh người tạo', default='anh_nguoi_tao.jpg')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'bộ sưu tập'
        verbose_name_plural = 'Quản lý bộ sưu tập'


