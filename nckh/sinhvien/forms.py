from django import forms
from django.utils.text import slugify
from .models import SinhVien

class SinhVienForm(forms.ModelForm):
    class Meta:
        model = SinhVien
        fields = ['msv', 'name', 'slug', 'gender', 'age', 'grade']

    def clean(self):
        cleaned_data = super().clean()  # Lấy dữ liệu đã được làm sạch từ form

        name = cleaned_data.get('name')  # Lấy tên người dùng nhập vào
        if name:
            # Tạo slug từ name bằng cách sử dụng slugify()
            slug = slugify(name)
            cleaned_data['slug'] = slug  # Đặt slug vào cleaned_data

        return cleaned_data
