from django.urls import path
from TiendaGuichoApp import views

urlpatterns = [
    path('', views.accesorios),
    path('accesorios/', views.accesorios, name="Accesorios"),
    path('calzado/', views.calzado, name="Calzado"),
    path('ropa/', views.ropa, name="Ropa"),
    path('correo/', views.correo, name="Correo"),
]