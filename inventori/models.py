from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Barang(models.Model):
    barang_id = models.AutoField(primary_key=True)
    barang_nama = models.CharField(max_length=255)
    barang_brand = models.CharField(max_length=255)
    barang_jenis = models.CharField(max_length=255)
    barang_spek = models.CharField(max_length=500)
    barang_created = models.DateTimeField(auto_now_add=True)
    barang_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.barang_nama, self.barang_brand)

class Inventaris(models.Model):
    INV_STATUS = [
        ('aktif', 'Aktif'),
        ('rusak', 'Rusak'),
        ('hilang', 'Hilang'),
        ('dilelang', 'Dilelang'),
    ]

    inv_id = models.AutoField(primary_key=True)
    inv_barang_id = models.ForeignKey(Barang, on_delete=models.CASCADE)
    inv_nomor = models.CharField(max_length=100)
    inv_pengadaan_petugas = models.CharField(max_length=255)
    inv_pengadaan_tgl = models.DateTimeField(blank=True, null=True)
    inv_pengadaan_harga = models.FloatField()
    inv_perbaikan_petugas = models.CharField(max_length=255)
    inv_perbaikan_tgl = models.DateTimeField(blank=True, null=True)
    inv_lokasi = models.CharField(max_length=255)
    inv_status = models.CharField(max_length=10, choices=INV_STATUS, default='aktif')
