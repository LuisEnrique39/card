from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decimal import Decimal
from django.db.models import Sum
import json
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.http import JsonResponse
from apps.home.models import Proyecto,UserInfo
from .models import Notificacion
from .models import Information
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
# para lo del token
from django.utils.crypto import get_random_string
from apps.home.models import CredentialToken




@login_required
def peticiones(request):
    notificaciones = Notificacion.objects.filter(leida=False).order_by('-fecha_creacion')[:3]
    num_notificaciones_no_leidas = notificaciones.count()

    peticiones = Notificacion.objects.order_by('-fecha_creacion')
    # Crear un objeto Paginator con proyectos y definir cuántos proyectos por página deseas mostrar (en este caso, 2)
    paginator = Paginator(peticiones, 5)

    # Obtener el número de página actual de la solicitud GET
    page_number = request.GET.get('page')

    # Obtener la página actual del Paginator
    peticiones_pagina = paginator.get_page(page_number)
    context = {'notificaciones': notificaciones, 'peticiones': peticiones_pagina,'num_notificaciones': num_notificaciones_no_leidas}
    return render(request, 'cliente/peticiones.html', context)


def information(request, id):
    u = User.objects.get(id = id)
    template = 'home/information.html'
    context = {'user':u}
    return render(request, template, context)

def update(request, id):
    if request.method == 'POST':
        id_user=id
        print(id_user)
        usersel = User.objects.get(id = id)
        print(usersel)
        info, created = Information.objects.get_or_create(user=usersel.id)
        # Actualiza la información del usuario del objeto info 
        info.first_name = request.POST['first_name']
        info.last_name = request.POST['last_name']
        info.telefono = request.POST['telefono']
        info.telefono_casa = request.POST['telefono_casa']
        info.nacimiento = request.POST['nacimiento']
        info.direccion = request.POST['direccion']
        info.puesto = request.POST['puesto']
        info.contacto_emergencia = request.POST['contacto_emergencia']
        info.telefono_emergencia = request.POST['telefono_emergencia']
        info.departamento = request.POST['departamento']
        info.save()

        toke, created = CredentialToken.objects.get_or_create(user_id=usersel.id)
        if created or not toke.token:
            toke.token = get_random_string(length=20)
            toke.save()

        return redirect('information', id=id)

@login_required
def pages(request):
    context = {}

    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
