from django.urls import path
from . import  views
app_name="Ramadhan"

urlpatterns = [
    path('', views.readJADWAL_IMSAKIYAH_1444_H),
    path('alamat/<int:id>', views.readJADWAL_IMSAKIYAH_1444_H),
    path('buat/', views.createJADWAL_IMSAKIYAH_1444_H),
    path('edit/<int:id>', views.updateJADWAL_IMSAKIYAH_1444_H),
    path('hapus.<int:id>', views.deleteJADWAL_IMSAKIYAH_1444_H),

]