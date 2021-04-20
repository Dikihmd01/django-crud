from django.shortcuts import render, redirect, HttpResponse
from perpus.models import *
from perpus.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from perpus.resource import BukuResource

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan buku.xls"'
    return response

def buku(request):
    books = Buku.objects.all
    konteks = {
        'books': books,
    }
    return render (request, "buku.html", konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()

            konteks = {
                'form': form,
                'pesan': 'Data berhasil disimpan!',
            }
            
            return render(request, 'tambah-buku.html', konteks)

    else:
        form = FormBuku()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'

    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)

        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah!")
            return redirect('ubah_buku', id_buku=id_buku)
    
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form': form,
            'buku': buku,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.error(request, "Data telah berhasil dihapus!")

    return redirect('/buku')

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registrasi berhasil!")
            return redirect('signup')

        else:
            messages.error(request, "Terjadi kesalahan, silahkan coba lagi!")
            return redirect('signup')

    else:
        form = UserCreationForm()
        konteks = {
            'form': form,
        }
    return render(request, 'signup.html', konteks)

