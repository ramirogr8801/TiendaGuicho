from django.shortcuts import render
from . models import Calzado, Accesorios, Ropa
from django.db.models import Q

# Create your views here.

def accesorios(request):
    accesorio = Accesorios.objects.all().order_by('nombre')
    queryset = request.GET.get("buscar_accesorios")
    if queryset:
        accesorio = Accesorios.objects.filter(
            Q(nombre__contains= queryset) |
            Q(cantidad__iexact = queryset) |
            Q(precio__iexact = queryset)
        ).distinct()
    context = {'accesorios': accesorio}
    return render(request, 'accesorios.html', context)


def calzado(request):
    calzado = Calzado.objects.all().order_by('marca')
    queryset = request.GET.get("buscar_calzado")
    if queryset:
         calzado = Calzado.objects.filter(
             Q(tipo__iexact = queryset) |
             Q(marca__iexact = queryset) |
             Q(color__iexact = queryset) |
             Q(talla__iexact = queryset) |
             Q(precio__iexact = queryset) |
             Q(cantidad__iexact = queryset)
         ).distinct()
    context = {'calzados': calzado}
    return render(request, 'calzado.html', context)



def ropa(request):
    ropa = Ropa.objects.all().order_by('tipo')
    queryset = request.GET.get("buscar_ropa")
    if queryset:
        ropa = Ropa.objects.filter(
            Q(tipo__iexact = queryset) |
            Q(color__iexact = queryset) |
            Q(talla__iexact = queryset) |
            Q(precio__iexact = queryset) |
            Q(cantidad__iexact = queryset)
        ).distinct()
    context = {'ropas': ropa}
    return render(request, 'ropa.html', context)

def correo(request):
    return render (request, 'correo.html')

   