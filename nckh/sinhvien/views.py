from django.shortcuts import render,get_object_or_404,redirect
from .models import SinhVien
from .forms import SinhVienForm
import rdflib
import matplotlib.pyplot as plt
from rdflib import Graph, Literal
from rdflib.namespace import RDF, URIRef
from rdflib import Namespace
import seaborn as sns  # Thư viện seaborn cho màu sắc đẹp 
# Create your views here.
import os
from django.conf import settings
def sinhvien_list(request):
    sinhviens = SinhVien.objects.all()
    context = {
        'title': 'Danh sách sinh vien',
        'sinhviens': sinhviens,
    }
    return render(request, 'sinhvien/sinhvien_list.html',context )

def add_sinhvien(request):
    if request.method == 'POST':
        form = SinhVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(add_sinhvien)
    else: 
        form = SinhVienForm()
        
    context = {
        'title': 'Thêm sinh viên',
        'form': form,
    }
    return render(request,'sinhvien/add_sinhvien.html',context)


def edit_sinhvien(request,msv):
    sinhvien = get_object_or_404(SinhVien, msv = msv)
    if request.method == 'POST':
        form = SinhVienForm(request.POST, instance=sinhvien)
        if form.is_valid():
            form.save()
            return redirect('sinhvien_list')
    else:
        form = SinhVienForm(instance=sinhvien)
    
    context = {
        'title': 'Sửa thông tin sinh viên',
        'form': form,
    }
    return render(request,'sinhvien/edit_sinhvien.html',context)

def delete_sinhvien(request,msv):
    sinhvien = get_object_or_404(SinhVien, msv = msv)
    if request.method == 'POST':
        sinhvien.delete()
        return redirect('sinhvien_list')
    
    form = SinhVienForm(instance=sinhvien)
    context = {
        'title': 'Xóa sinh viên',
        'form': form,
    }

    return render(request, 'sinhvien/delete_sinhvien.html',context)

#  rdf lib hieenr thi diem sinh vien
def student_grades_rdf(request):  
    # Tạo một Graph RDF và khai báo Namespace  
    g = Graph()  
    ex = Namespace("http://example.org/")  

    # Lấy dữ liệu sinh viên từ cơ sở dữ liệu  
    students = SinhVien.objects.all()  

    # Thêm các thông tin vào Graph (RDF)  
    for student in students:  
        student_uri = ex[student.msv]  
        g.add((student_uri, RDF.type, ex.Student))  
        g.add((student_uri, ex.name, Literal(student.name)))  
        g.add((student_uri, ex.gender, Literal(student.gender)))  
        g.add((student_uri, ex.grade, Literal(student.grade)))  

    # Trích xuất thông tin điểm và tên từ RDF  
    grades = []  
    names = []  

    for student in g.subjects(RDF.type, ex.Student):  
        grade = g.value(student, ex.grade)  
        name = g.value(student, ex.name)  
        grades.append(float(grade))  # Chuyển đổi sang float  
        names.append(name)  

    # Sắp xếp theo điểm  
    sorted_data = sorted(zip(names, grades), key=lambda x: x[1])  
    names_sorted, grades_sorted = zip(*sorted_data)  

    # Sử dụng seaborn để vẽ biểu đồ cột  
    plt.figure(figsize=(12, 6))  # Kích thước biểu đồ  
    sns.barplot(x=names_sorted, y=grades_sorted, palette='Blues_d')  # Màu sắc đẹp  

    # Thêm nhãn cho các cột  
    for i, grade in enumerate(grades_sorted):  
        plt.text(i, grade + 0.02, round(grade, 2), ha='center', fontsize=10, color='black')  

    plt.xlabel('Sinh viên', fontsize=12)  
    plt.ylabel('Điểm', fontsize=12)  
    plt.title('Biểu đồ điểm của sinh viên', fontsize=14)  
    plt.xticks(rotation=45)  
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Đường lưới cho trục Y  

    # Lưu biểu đồ vào thư mục media  
    chart_path = os.path.join(settings.MEDIA_ROOT, 'grades_chart.png')  
    plt.savefig(chart_path)  
    plt.close()  # Đóng biểu đồ sau khi lưu  

    # Trả về trang HTML với URL của biểu đồ  
    grades_chart_url = '/media/grades_chart.png'  # Đảm bảo rằng đường dẫn chính xác  
    return render(request, 'sinhvien/student_grades_rdf.html', {'grades_chart_url': grades_chart_url})  