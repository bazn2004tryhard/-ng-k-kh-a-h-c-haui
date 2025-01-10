from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sinhvien_list, name='sinhvien_list'),  # Hiển thị danh sach sinh vien
    path('add/', views.add_sinhvien, name='add_sinhvien'),  # Thêm sinh vien mới
    path('edit/<str:msv>/', views.edit_sinhvien, name='edit_sinhvien'),  # Sửa thông tin sinh vien
    path('delete/<str:msv>/', views.delete_sinhvien, name='delete_sinhvien'),  # Xóa sinh vien
    path('students/grades/rdf/', views.student_grades_rdf, name='student_grades_rdf'),
]

# # Nếu DEBUG=True, Django sẽ phục vụ các tệp từ thư mục media
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)