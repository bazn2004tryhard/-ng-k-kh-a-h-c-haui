from django.urls import path
from . import views

urlpatterns = [
    path('', views.sinhvien_list, name='sinhvien_list'),  # Hiển thị danh sach sinh vien
    path('add/', views.add_sinhvien, name='add_sinhvien'),  # Thêm sinh vien mới
    path('edit/<str:msv>/', views.edit_sinhvien, name='edit_sinhvien'),  # Sửa thông tin sinh vien
    path('delete/<str:msv>/', views.delete_sinhvien, name='delete_sinhvien'),  # Xóa sinh vien
]