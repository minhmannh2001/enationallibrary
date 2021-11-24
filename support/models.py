from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length=50, verbose_name='Tên')
    lastName = models.CharField(max_length=50, verbose_name='Họ')
    emailAddress = models.CharField(max_length=100, verbose_name='Địa chỉ Email')
    subject = models.CharField(max_length=200, verbose_name='Tiêu đề')
    message = models.TextField(verbose_name='Nội dung câu hỏi')
    answer = RichTextField(null=True, blank=True, verbose_name='Nội dung phản hồi')
    NOT_ANSWER = 'NOT ANSWER'
    ANSWERED = 'ANSWERED'
    ANSWER_STATUS = [
        (NOT_ANSWER, 'Chưa trả lời'),
        (ANSWERED, 'Đã trả lời'),
    ]
    status = models.CharField(max_length=30, choices=ANSWER_STATUS, default='NOT ANSWER', verbose_name='Tình trạng')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'thư phản hồi'
        verbose_name_plural = 'Quản lý thư phản hồi'

