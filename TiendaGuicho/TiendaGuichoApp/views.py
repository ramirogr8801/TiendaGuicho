from django.shortcuts import render


# Create your views here.

def accesorios(request):
    return render (request, 'accesorios.html')

def prueba(request):
    return render (request, 'Prueba.html')