from django import forms
from django.core import validators
from .models import Barang, Inventaris


class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['barang_nama', 'barang_brand', 'barang_jenis', 'barang_spek']
        labels = {
            'barang_nama': 'Nama Barang',
            'barang_brand': 'Penyedia Barang',
            'barang_jenis': 'Jenis Barang',
            'barang_spek': 'Spesifikasi Barang',
        }
        widgets = {
            'barang_nama': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'barang_brand': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'barang_jenis': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'barang_spek': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }


class InvForm(forms.ModelForm):
    class Meta:
        model = Inventaris
        fields = ['inv_barang_id', 'inv_nomor', 'inv_pengadaan_petugas', 'inv_pengadaan_tgl', 'inv_pengadaan_harga',
                  'inv_perbaikan_petugas', 'inv_perbaikan_tgl', 'inv_lokasi', 'inv_status']
        labels = {
            'inv_barang_id': 'Barang',
            'inv_nomor': 'Nomor Inventaris',
            'inv_pengadaan_petugas': 'Nama Petugas',
            'inv_pengadaan_tgl': 'Tanggal Pengadaan',
            'inv_pengadaan_harga': 'Harga Saat Pengadaan',
            'inv_perbaikan_petugas': 'Petugas Perbaikan',
            'inv_perbaikan_tgl': 'Tanggal Perbaikan',
            'inv_lokasi': 'Lokasi Inventaris',
            'inv_status': 'Status Inventaris',
        }
        widgets = {
            'inv_barang_id': forms.Select(attrs={'class': 'form-control'}),
            'inv_nomor': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'inv_pengadaan_petugas': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'inv_pengadaan_tgl': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'inv_pengadaan_harga': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'inv_perbaikan_petugas': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'inv_perbaikan_tgl': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'inv_lokasi': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'inv_status': forms.Select(attrs={'class': 'form-control'}),
        }
