from django.db import models
from django.utils.text import slugify
# Create your models here.
class SinhVien(models.Model):
    CHOICE_GENDER = (
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ')
    )
    msv = models.CharField(unique=True, primary_key=True,max_length=250)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True,max_length=250,blank=True)
    gender = models.CharField(max_length=10, choices=CHOICE_GENDER)
    age = models.IntegerField()
    grade = models.FloatField()  # Điểm trung bình

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Nếu slug chưa được cung cấp, tự động tạo slug từ name
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)