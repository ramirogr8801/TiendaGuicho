from django.shortcuts import render
from . models import Calzado, Accesorios, Ropa

# Create your views here.

def accesorios(request):
    accesorio = Accesorios.objects.all().order_by('nombre')
    context = {'accesorios': accesorio}
    return render(request, 'accesorios.html', context)

def calzado(request):
    calzado = Calzado.objects.all().order_by('marca')
    context = {'calzados': calzado}
    return render(request, 'calzado.html', context)

def ropa(request):
    ropa = Ropa.objects.all().order_by('tipo')
    context = {'ropas': ropa}
    return render(request, 'ropa.html', context)

def correo(request):
    return render (request, 'correo.html')

   