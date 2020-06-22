from django.shortcuts import render
from . models import Calzado, Accesorios, Ropa
from django.db.models import Q
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def accesorios(request):
    accesorio = Accesorios.objects.all().order_by('nombre')
    queryset = request.GET.get("buscar_accesorios")
    
    if request.method == 'POST':
        chequed = request.POST.getlist('accesorios_selected')
        if chequed:
            context = {'accesorios': accesorio,
                       'chequed':chequed}
            # print(type(chequed))
            return render (request,  'correo.html', context)
    
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
    
    if request.method == 'POST':
        chequed = request.POST.getlist('calzados_selected')
        if chequed:
            context = {'calzados': calzado,
                       'chequed':chequed}
            # print(type(chequed))
            return render (request,  'correo.html', context)
    
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
    
    if request.method == 'POST':
        chequed = request.POST.getlist('ropas_selected')
        if chequed:
            context = {'ropas': ropa,
                       'chequed':chequed}
            return render (request,  'correo.html', context)

    if queryset:
        ropa = Ropa.objects.filter(
            Q(tipo__iexact = queryset) |
            Q(color__iexact = queryset) |
            Q(talla__iexact = queryset) |
            Q(precio__iexact = queryset) |
            Q(cantidad__iexact = queryset)
        ).distinct()
    context = {'ropas': ropa}
    
    return render (request, 'ropa.html', context)

# def enviar_correo(request):
#     if request.method == 'POST':
#         first_name = request.POST['nombre']
#         last_name = request.POST['apellido']
#         subject = request.POST['subject']
#         to_email = request.POST['client_email']
#         body = request.POST['mensaje']
        
#         message = Mail(
#             from_email = 'tiendaguichodeportes@guicho.com',
#             to_emails = to_email,
#             subject = subject,
#             html_content='Hola' + first_name + last_name +', los productos' + body + 'han sido enviados.')
#         try:
#             sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#             response = sg.send(message)
#             print(response.status_code)
#             print(response.body)
#             print(response.headers)
#         except Exception as e:
#             print(e.message)
        
#         return render (request,'mail_sended.html')
    
#     return render (request, 'correo.html')

def enviar_correo(request):
    if request.method == 'POST':
        first_name = request.POST['nombre_cliente']
        last_name = request.POST['apellido_cliente']
        # subject = request.POST['subject']
        subject = 'Correo sobre productos aquiridos en deportes Guicho'
        message = 'Hola'+ " " + first_name + " " + last_name + " " + ', usted acaba de adquirir los siguientes productos:' + " "+ request.POST['msg']
        print(message)
        from_email = settings.EMAIL_HOST_USER
        to_mail = [request.POST['client_email']]
        context = {
            'nombre': first_name,
            'apellido': last_name,
            
        }
        
        send_mail(subject, message, from_email, to_mail)
        
        return render (request,'mail_sended.html', context)
    
    return render (request, 'correo.html')

   