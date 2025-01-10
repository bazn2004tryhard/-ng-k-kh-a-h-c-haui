from django.shortcuts import render,get_object_or_404,redirect
from .models import SinhVien
from .forms import SinhVienForm
# Create your views here.

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

