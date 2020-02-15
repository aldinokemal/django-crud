from django.urls import path
from . import views

app_name = 'inventori'
urlpatterns = [
    path('', views.redirect_barang, name="index"),
    path('barang/', views.barang_show, name="barang.show"),
    path('barang/add', views.barang_add, name="barang.add"),
    path('barang/delete/<int:id>', views.barang_delete, name="barang.del"),
    path('barang/edit/<int:id>', views.barang_edit, name="barang.edit"),
    path('inventori/', views.inv_show, name="inv.show"),
    path('inventori/add', views.inv_add, name="inv.add"),
    path('inventori/edit/<int:id>', views.inv_edit, name="inv.edit"),
    path('inventori/delete/<int:id>', views.inv_delete, name="inv.del"),
]
