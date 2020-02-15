from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BarangForm, InvForm
from .models import Barang, Inventaris


# Create your views here.
@login_required
def redirect_barang(request):
    return redirect("inventori:barang.show")


# ============================== HALAMAN BARANG
@login_required
def barang_show(request):
    data = Barang.objects.all()
    return render(request, "barang.html", {'datas': data})


@login_required
def barang_add(request):
    if request.method == 'POST':
        form = BarangForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Barang berhasil ditambahkan')
            return redirect('inventori:barang.show')
        else:
            messages.error(request, 'Terjadi Kesalahan')
    else:
        form = BarangForm()
        return render(request, "barang_add.html", {'form': form})


@login_required
def barang_edit(request, id):
    barang = Barang.objects.get(barang_id=id)
    form = BarangForm(request.POST, instance=barang)
    if form.is_valid():
        form.save()
        messages.success(request, 'Barang berhasil diperbarui')
        # return redirect("inventori:barang.edit", id=id)
        return redirect("inventori:barang.show")
    return render(request, "barang_edit.html", {'barang': barang})


@login_required
def barang_delete(request, id):
    barang = Barang.objects.get(barang_id=id)
    barang.delete()
    return redirect("inventori:barang.show")


# ============================== HALAMAN INVENTARIS
@login_required
def inv_show(request):
    data = Inventaris.objects.all()
    return render(request, "inventaris.html", {'datas': data})


@login_required
def inv_add(request):
    if request.method == 'POST':
        form = InvForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Barang berhasil ditambahkan')
            return redirect('inventori:inv.show')
        else:
            messages.error(request, 'Terjadi Kesalahan')
    else:
        form = InvForm()
        return render(request, "inventaris_add.html", {'form': form})


def inv_edit(request, id):
    data = Inventaris.objects.get(inv_id=id)

    if request.method == 'POST':
        form = InvForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inventaris berhasil diperbarui')
            # return redirect("inventori:barang.edit", id=id)
            return redirect("inventori:inv.show")
    else:
        form = InvForm(instance=data)
        return render(request, "inventaris_edit.html", {'data': data, 'form': form})


def inv_delete(request, id):
    inventaris = Inventaris.objects.get(inv_id=id)
    inventaris.delete()
    return redirect("inventori:barang.show")
