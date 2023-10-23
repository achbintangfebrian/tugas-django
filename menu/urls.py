from django.urls import path
from . import views

urlpatterns = [
    path('beranda/', views.beranda, name='beranda'),
    path('kelas/', views.kelas, name='kelas'),
    path('jadwal/', views.jadwal, name='jadwal'),
]