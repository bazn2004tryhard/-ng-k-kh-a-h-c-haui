from django.contrib import admin

# Register your models here.
from .models import SinhVien

class SinhVienAdmin(admin.ModelAdmin):
    list_display = ('msv','name','slug','gender','age','grade')

admin.site.register(SinhVien, SinhVienAdmin)