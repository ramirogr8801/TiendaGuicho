from django.shortcuts import render


# Create your views here.

def inicio(request):
    return render (request, 'Inicio.html')

def prueba(request):
    return render (request, 'Prueba.html')