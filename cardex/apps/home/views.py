from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import SolicitudVacaciones, UserInfo,Proyecto #por revisar para eliminar
from apps.cliente.models import Notificacion
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decimal import Decimal
from django.db.models import Sum
import json
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.http import JsonResponse
from django.utils import timezone
from . import models
from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
import qrcode
from io import BytesIO
from django.core.exceptions import ObjectDoesNotExist
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from apps.cliente.forms import PostForm
from .models import AsignacionHat,Hat, Egresos, CredentialToken,Document,Justificantesmedicos,Vacaciones
from apps.cliente.models import Post,Information,Profile

from .models import Vacaciones
from django.utils.translation import gettext as _


@login_required
def index(request, username=None):
    html_template = loader.get_template('home/index.html')
    if request.user.is_authenticated:
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            posts = user.posts.all().exclude(activate = "False")
            
        else:
            posts = current_user.posts.all().exclude(activate = "False")
            user = current_user
            
            
        paginator = Paginator(posts, 10)  # 10 registros por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_num = page_obj.number
        max_pages_before_and_after = 2
        page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

        context = {'user': user, 'posts': page_obj, 'page_numbers': page_numbers}
        return HttpResponse(html_template.render(context, request))
    else:
        return render(request, template)
        return HttpResponse(html_template.render(request))
    
def calcular_dias_de_vacaciones(ingreso, fecha_actual):
    if not ingreso or not fecha_actual:
        return 0  # No hay ingreso o fecha actual, no se pueden calcular vacaciones

    fecha_ingreso = datetime.strptime(ingreso, '%Y-%m-%d')
    fecha_actual = datetime.strptime(fecha_actual, '%Y-%m-%d')

    # Calcular la diferencia en años entre ingreso y fecha actual
    diferencia = relativedelta(fecha_actual, fecha_ingreso)

    # Definir la asignación de días de vacaciones según la antigüedad
    if diferencia.years == 1:
        dias_vacaciones = 12
    elif diferencia.years == 2:
        dias_vacaciones = 14
    elif diferencia.years == 3:
        dias_vacaciones = 16
    elif diferencia.years == 4:
        dias_vacaciones = 18
    elif diferencia.years >= 5:
        dias_vacaciones = 20
    else:
        dias_vacaciones = 0  # Si la antigüedad es menor a 1 año, no se asignan vacaciones

    return dias_vacaciones


@login_required
def profileg(request,username=None):
    user = User.objects.get(username=username)
    user = request.user  # Obtener el usuario actual
    current_user = request.user
    hat = Hat.objects.order_by('id')
    holydays = Vacaciones.objects.filter(user=user).first()
    periodo = Egresos.objects.filter(user=user).first()  # Obtener el objeto de egresos

    dias_transcurridos = None  # Para manejar el caso en que no haya un período definido
    anios_transcurridos = None
    meses_transcurridos = None
    
    dias_transcurridos_actual = None  # Para manejar el caso en que no haya un período definido
    anios_transcurridos_actual = None
    meses_transcurridos_actual = None
    tiempo_transcurrido_hasta_ahora = None
    tiempo_formateado = None  # Definir tiempo_formateado como None
    anios_transcurridos = None

    periodo = Egresos.objects.filter(user=user).first() #me filtra por usuario y ya no por la sesion actual
    if periodo and periodo.ingreso:
        try:
            fecha_ingreso = datetime.strptime(periodo.ingreso, '%Y-%m-%d')
            fecha_actual = datetime.now()
            diferencia = fecha_actual.year - fecha_ingreso.year
            anios_transcurridos = diferencia
        except ValueError as e:
            print("Error al calcular los años transcurridos:", e)

    if periodo and periodo.ingreso:
        fecha_actual = timezone.now().strftime('%Y-%m-%d')  # Obtener la fecha actual en formato de cadena
        dias_de_vacaciones = calcular_dias_de_vacaciones(periodo.ingreso, fecha_actual)
    else:
        dias_de_vacaciones = 0  # No se pueden calcular vacaciones sin fecha de ingreso

    # Actualiza o crea un registro de días de vacaciones en el modelo Vacaciones
    vacaciones, created = Vacaciones.objects.get_or_create(user=user)
    vacaciones.dias = dias_de_vacaciones
    vacaciones.save()
    if periodo and periodo.ingreso:  # Verifica si ya existe el periodo
        try:
            fecha_ingreso = timezone.make_aware(datetime.strptime(periodo.ingreso, '%Y-%m-%d'), timezone.utc)
            fecha_actual = timezone.now()
            
            diferencia_actual = relativedelta(fecha_actual, fecha_ingreso)
            anios_transcurridos_actual = diferencia_actual.years
            meses_transcurridos_actual = diferencia_actual.months
            dias_transcurridos_actual = diferencia_actual.days
            print("Años (hasta ahora):", anios_transcurridos_actual)
            print("Meses (hasta ahora):", meses_transcurridos_actual)
            print("Días (hasta ahora):", dias_transcurridos_actual)
            tiempo_transcurrido_hasta_ahora = fecha_actual - fecha_ingreso
            print("Tiempo transcurrido hasta ahora:", tiempo_transcurrido_hasta_ahora)
            
            dias = tiempo_transcurrido_hasta_ahora.days
            horas, segundos = divmod(tiempo_transcurrido_hasta_ahora.seconds, 3600)
            minutos, segundos = divmod(segundos, 60)
            
            tiempo_formateado = {
                'dias': dias,
                'horas': horas,
                'minutos': minutos,
                'segundos': segundos,
            }
            
            if periodo.egreso:  # Si hay egreso, calcula la diferencia de tiempo con egreso
                fecha_egreso = timezone.make_aware(datetime.strptime(periodo.egreso, '%Y-%m-%d'), timezone.utc)
                diferencia = relativedelta(fecha_egreso, fecha_ingreso)
                anios_transcurridos = diferencia.years
                meses_transcurridos = diferencia.months
                dias_transcurridos = diferencia.days
                print("Años (con egreso):", anios_transcurridos)
                print("Meses (con egreso):", meses_transcurridos)
                print("Días (con egreso):", dias_transcurridos)
        except ValueError as e:  # Excepciones
            print("Error al convertir las fechas:", e)
    if dias_transcurridos_actual is not None:
        anios_transcurridos_actual = dias_transcurridos_actual // 365
    
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
        asignados = AsignacionHat.objects.filter(user_id=user.id)
        cantidad_registros = asignados.count()
        print(cantidad_registros)
    else:
        posts = current_user.posts.all()
        user = current_user
        asignados = AsignacionHat.objects.filter(user_id=current_user.id)
        cantidad_registros = asignados.count()
    id = str(user.id)
    reset(user.id)
    
    # Convertir la fecha actual a años
    if anios_transcurridos_actual is None:
        fecha_actual = datetime.now()
        fecha_ingreso = datetime.strptime(periodo.ingreso, '%Y-%m-%d')
        diferencia_actual = relativedelta(fecha_actual, fecha_ingreso)
        anios_transcurridos_actual = diferencia_actual.years

    
    
    context = {'user': user, 'posts': posts, 'hat': hat, 'registros': asignados, 
        'cantidad_registros': cantidad_registros, 
        'periodo': periodo, 
        'tiempo_formateado': tiempo_formateado,
        'dias_transcurridos': dias_transcurridos, 
        'anios_transcurridos': anios_transcurridos,
        'meses_transcurridos': meses_transcurridos, 
        'tiempo_transcurrido_hasta_ahora': tiempo_transcurrido_hasta_ahora,
        'dias_transcurridos_actual': dias_transcurridos_actual,
        'anios_transcurridos_actual': anios_transcurridos_actual,
        'meses_transcurridos_actual': meses_transcurridos_actual,
        'dias_de_vacaciones': dias_de_vacaciones,
        'holydays': holydays,}
    return render(request, "home/profile.html", context)

def asignar_vacaciones(request, user_id):
    user = User.objects.get(id=user_id)
    inicio = request.POST.get('inicio')
    final = request.POST.get('final')
    periodo = Egresos.objects.filter(user=user).first()
    holydays = Vacaciones.objects.filter(user=user).first()

    anios_transcurridos = None

    if periodo and periodo.ingreso:
        try:
            fecha_ingreso = datetime.strptime(periodo.ingreso, '%Y-%m-%d')
            fecha_actual = datetime.now()
            diferencia = fecha_actual.year - fecha_ingreso.year
            anios_transcurridos = diferencia
        except ValueError as e:
            print("Error al calcular los años transcurridos:", e)

    if request.method == 'POST' and inicio and final:
        inicio = datetime.strptime(inicio, '%m/%d/%Y').date()
        final = datetime.strptime(final, '%m/%d/%Y').date()
        dias_vacaciones_usados = contar_dias_habiles(inicio, final)

        if dias_vacaciones_usados < 1:
            messages.error(request, _("No hay días hábiles entre las fechas seleccionadas."))
            return JsonResponse({'success': False, 'message': 'No hay días hábiles entre las fechas seleccionadas.'})
        elif inicio > final:
            messages.error(request, _("La fecha de inicio debe ser anterior a la fecha final."))
            return JsonResponse({'success': False, 'message': 'La fecha de inicio debe ser anterior a la fecha final.'})
        else:
            dias_utilizados_anteriores = SolicitudVacaciones.objects.filter(user=user).aggregate(Sum('dias_usados'))['dias_usados__sum'] or 0
            dias_restantes = user.vacaciones.dias - (dias_vacaciones_usados + dias_utilizados_anteriores)

            anios_servicio = anios_transcurridos

            solicitud = SolicitudVacaciones(user=user, inicio=inicio, final=final, dias_usados=dias_vacaciones_usados)
            solicitud.dias_restantes = dias_restantes
            solicitud.anios_servicio = anios_servicio
            solicitud.save()

            # Permite la redirección incluso si los días restantes son 0
            return JsonResponse({'success': True, 'message': 'descarga el pdf.'})

    ultima_solicitud = SolicitudVacaciones.objects.filter(user=user).order_by('-id').first()
    print(f'Última solicitud: {ultima_solicitud}')

    if ultima_solicitud is not None:
        inicio = ultima_solicitud.final

        if inicio.weekday() == 4:
            nueva_fecha = inicio + timedelta(days=3)
        elif inicio.weekday() >= 0 and inicio.weekday() <= 3:
            nueva_fecha = inicio + timedelta(days=1)
        else:
            nueva_fecha = inicio
    else:
        nueva_fecha = None
        messages.error(request, _("Selecciona una fecha"))

    return render(request, 'home/asignar_vacaciones.html', {'holydays': holydays, 'anios_transcurridos': anios_transcurridos, 'periodo': periodo, 'user_id': user_id, 'user': user, 'ultima_solicitud': ultima_solicitud, 'nueva_fecha': nueva_fecha})

def reset(id_u):
    user = User.objects.get(id=id_u)
    print(user.id)
    periodo = Egresos.objects.filter(user_id=user.id).first()
    print(periodo)
    holydays = SolicitudVacaciones.objects.filter(user_id=user.id).last()
    print(holydays)

    anios_transcurridos = None

    if periodo and periodo.ingreso:
        try:
            fecha_ingreso = datetime.strptime(periodo.ingreso, '%Y-%m-%d')
            fecha_actual = datetime.now()
            diferencia = fecha_actual.year - fecha_ingreso.year
            anios_transcurridos = diferencia
        except ValueError as e:
            print("Error al calcular los años transcurridos:", e)

    if holydays is not None:
        if anios_transcurridos > holydays.anios_servicio:
            Vacaciones = SolicitudVacaciones.objects.filter(user_id=user.id)
            Vacaciones.delete()
            print("Entre al if")
def contratos (request, user_id=None):
    user = User.objects.get(id=user_id)
    template = 'home/CONTRATO_INDIVIDUALpdf.html'
    context = {'user':user}
    
    return render(request, template, context)

def asignar_vacacionespdf(request, user_id=None):
    user = User.objects.get(id=user_id)
    periodo = Egresos.objects.filter(user=user).first()
    holydays = Vacaciones.objects.filter(user=user).first()
    holas = SolicitudVacaciones.objects.filter(user=user).order_by('-id').first()
    ultima_solicitud = SolicitudVacaciones.objects.filter(user=user).order_by('-id').first()
    hola = SolicitudVacaciones.objects.filter(user=user).order_by('-id').first()

    anios_transcurridos = None

    if periodo and periodo.ingreso:
        try:
            fecha_ingreso = datetime.strptime(periodo.ingreso, '%Y-%m-%d')
            fecha_actual = datetime.now()
            diferencia = fecha_actual.year - fecha_ingreso.year
            anios_transcurridos = diferencia
        except ValueError as e:
            print("Error al calcular los años transcurridos:", e)

    if ultima_solicitud is not None:
        inicio = ultima_solicitud.final  # Comienza desde la fecha final de la última solicitud

        # Verificar si el último día de solicitud es viernes (4 representa viernes)
        if inicio.weekday() == 4:
            # Agregar tres días al calendario si es viernes
            nueva_fecha = inicio + timedelta(days=3)
        elif inicio.weekday() >= 0 and inicio.weekday() <= 3:
            # Agregar un día adicional al calendario si es de lunes a jueves
            nueva_fecha = inicio + timedelta(days=1)
        else:
            nueva_fecha = inicio
    else:
        # Manejar el caso en el que la última solicitud es None
        nueva_fecha = None
        messages.error(request, "Selecciona una fecha")

    template = 'home/asignar_vacacionespdf.html'
    context = {'user': user, 'periodo': periodo, 'holydays': holydays, 'ultima_solicitud': ultima_solicitud, 'hola': hola, 'holas': holas, 'nueva_fecha': nueva_fecha, 'anios_transcurridos': anios_transcurridos}
    return render(request, template, context)



def asignarhat(request,user_id=None):
    template = 'home/asignarhat.html'
    hat = Hat.objects.order_by('id')
    u = User.objects.get(id = user_id)

    if request.method == "POST":
        print(user_id)
        asig = AsignacionHat.objects.create(
                  user_id=request.POST['user_id'], hat_id = request.POST['hat_id'])
        asig.save()

    context = {'hat': hat,'user':u}
    return render(request, template, context)

@login_required
def asignaregreso(request, user_id=None):
    template = 'home/asignar_egreso.html'
   
    id_user=user_id
   
    periodo_existente = Egresos.objects.filter(user_id=id_user).first()
   
    if request.method == 'POST':
        ingreso = request.POST.get('ingreso', None)
        egreso = request.POST.get('egreso', None)
        id = request.POST.get('id', None)
      
        if periodo_existente:
            # Solo actualiza la fecha de ingreso si se proporciona una nueva fecha
            if ingreso:
                periodo_existente.ingreso = ingreso
            periodo_existente.egreso = egreso if egreso else None
            periodo_existente.save()
            messages.success(request, "Periodo actualizado con éxito")
        else:
            Egresos.objects.create(
                user_id=id_user,
                ingreso=ingreso,
                egreso=egreso if egreso else None
        
            )
            messages.success(request, "Periodo asignado con éxito")

        return redirect('home')

    context = {'id_user':id_user}
    return render(request, template, context)
######esto es de asignar vacaciones
def contar_dias_habiles(inicio, final):
    def es_dia_habil(fecha):
        if fecha.weekday() >= 5:  # 5 representa sábado, 6 representa domingo
            return False
        return True

    dias_habiles = 0
    fecha_actual = inicio
    while fecha_actual <= final:
        if es_dia_habil(fecha_actual):
            dias_habiles += 1
        fecha_actual += timedelta(days=1)
    return dias_habiles


def asignar_vacaciones(request, user_id):
    user = User.objects.get(id=user_id)
    inicio = request.POST.get('inicio')
    final = request.POST.get('final')
    periodo = Egresos.objects.filter(user=user).first()
    holydays = Vacaciones.objects.filter(user=user).first()

    anios_transcurridos = None

    if periodo and periodo.ingreso:
        try:
            fecha_ingreso = datetime.strptime(periodo.ingreso, '%Y-%m-%d')
            fecha_actual = datetime.now()
            diferencia = fecha_actual.year - fecha_ingreso.year
            anios_transcurridos = diferencia
        except ValueError as e:
            print("Error al calcular los años transcurridos:", e)
    if request.method == 'POST' and inicio and final:
        inicio = datetime.strptime(inicio, '%Y-%m-%d').date()
        final = datetime.strptime(final, '%Y-%m-%d').date()
        dias_vacaciones_usados = contar_dias_habiles(inicio, final)

        if dias_vacaciones_usados < 1:
            messages.error(request, _("No hay días hábiles entre las fechas seleccionadas."))
            return JsonResponse({'success': False, 'message': 'No hay días hábiles entre las fechas seleccionadas.'})
        elif inicio > final:
            messages.error(request, _("La fecha de inicio debe ser anterior a la fecha final."))
            return JsonResponse({'success': False, 'message': 'La fecha de inicio debe ser anterior a la fecha final.'})
        else:
            # Esta línea debe estar correctamente indentada
            dias_utilizados_anteriores = SolicitudVacaciones.objects.filter(user=user).aggregate(Sum('dias_usados'))['dias_usados__sum'] or 0

        # Resto del código...

            dias_restantes = user.vacaciones.dias - (dias_vacaciones_usados + dias_utilizados_anteriores)

            if dias_restantes < 0:
                messages.error(request, _("No hay suficientes días de vacaciones restantes."))
                return JsonResponse({'success': False, 'message': 'No hay suficientes días de vacaciones restantes.'})

            anios_servicio = anios_transcurridos

            solicitud = SolicitudVacaciones(user=user, inicio=inicio, final=final, dias_usados=dias_vacaciones_usados)
            solicitud.dias_restantes = dias_restantes
            solicitud.anios_servicio = anios_servicio
            solicitud.save()

            # Permite la redirección incluso si los días restantes son 0
            return JsonResponse({'success': True, 'message': 'descarga el pdf.'})

    ultima_solicitud = SolicitudVacaciones.objects.filter(user=user).order_by('-id').first()
    print(f'Última solicitud: {ultima_solicitud}')

    if ultima_solicitud is not None:
        inicio = ultima_solicitud.final

        if inicio.weekday() == 4:
            nueva_fecha = inicio + timedelta(days=3)
        elif inicio.weekday() >= 0 and inicio.weekday() <= 3:
            nueva_fecha = inicio + timedelta(days=1)
        else:
            nueva_fecha = inicio
    else:
        nueva_fecha = None
        messages.error(request, _("Selecciona una fecha"))

    return render(request, 'home/asignar_vacaciones.html', {'holydays': holydays, 'anios_transcurridos': anios_transcurridos, 'periodo': periodo, 'user_id': user_id, 'user': user, 'ultima_solicitud': ultima_solicitud, 'nueva_fecha': nueva_fecha})



@login_required
def eliminar_foto(request):
    user_info = UserInfo.objects.get(user=request.user)

    # Elimina la foto de perfil anterior si existe
    if user_info.foto_de_perfil:
        fs = FileSystemStorage(location=settings.STATICFILES_DIRS[0])
        previous_image_path = os.path.join(fs.location, user_info.foto_de_perfil.name)
        if os.path.isfile(previous_image_path):
            os.remove(previous_image_path)

        # Borra el registro de la foto de perfil en la base de datos
        user_info.foto_de_perfil = None
        user_info.save()

        return JsonResponse({"message": "La foto de perfil se eliminó con éxito."})
    else:
        return JsonResponse({"message": "No hay foto de perfil para eliminar."})

def pendiente(request):
    profile, created = Profile.objects.get_or_create(user_id=request.user)
    all_foto= Profile.objects.all()
    print(all_foto)
    notificaciones = Notificacion.objects.filter(leida=False).order_by('-fecha_creacion')[:3]
    num_notificaciones_no_leidas = notificaciones.count()

    if request.method == 'POST':
        print(request.POST)
        # Manejar la imagen de perfil
        foto_de_perfil = request.FILES.get('foto_de_perfil')
        
        

        # Guarda la nueva foto de perfil en la carpeta adecuada
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save('assets/img/perfil/' + foto_de_perfil.name, foto_de_perfil)
        profile.image = filename

        profile.save()
        return redirect('profile')  # Redirige de nuevo a la página de perfil después de la actualización

#qrs
def generar_codigo_qr(request, user_id):
    try:
        id_user=user_id
        # Obtén el usuario correspondiente al user_id
        usuario = CredentialToken.objects.get(user_id=id_user)
        token_user= usuario.token
        print(usuario)
        print(token_user)
        # Construye la URL de la credencial del usuario cardex.tescacorporation.com
        
        url_credencial = reverse('credencial',args=[token_user])
        print(url_credencial)

        # Genera el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(request.build_absolute_uri(url_credencial))
        qr.make(fit=True)

        # Crea una imagen del código QR
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        image_data = buffer.getvalue()

        # Devuelve la imagen como respuesta HTTP
        return HttpResponse(image_data, content_type="image/png")
    except CredentialToken.DoesNotExist:
        # Manejar el caso en el que el usuario no exista
        return HttpResponse("Usuario no encontrado", status=404)

def credencial(request, tokenid=None):
    template = 'home/credenciales/credencial.html'
    token1= tokenid
    token2 = CredentialToken.objects.get(token=token1)
    usuario = token2.user_id
    user = User.objects.get(id=token2.user_id)
    puesto = AsignacionHat.objects.filter(user_id=usuario)
    hats = Hat.objects.all()
    context = {'user': user, 'puesto': puesto, 'hats':hats}
    return render(request, template, context)


###################### menu ######################
def perfil_general(request, username=None):
    template = 'home/profgen.html'
    users = User.objects.all().exclude(is_active = "False")
    
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]
    
    context = {'users': page_obj,'page_numbers': page_numbers}
    
    return render(request, template, context)

def asistencia(request):
    template = 'home/asistencias.html'
    posts = Post.objects.filter(activate=True)
    users = User.objects.all()

    variable = request
    for intento in variable:
        current_user = get_object_or_404(User, pk=request.user.pk)
        current_user2 = (request.user.information.first_name + " " + request.user.information.last_name  )

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.fullname = current_user2
            post.save()
            
    else:
        form = PostForm()
    
    search_query = request.GET.get('search')
    if search_query:
                 posts = posts.filter(
                    Q(content__icontains=search_query) |
                    Q(fullname__icontains=search_query) |
                    Q(status__icontains=search_query) |
                    Q(Fecha__icontains=search_query) |
                    Q(entrada__icontains=search_query)
                    )
            
    paginator = Paginator(posts, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

    context = {'posts': page_obj,'users': users, 'page_numbers': page_numbers, 'form': form}
    return render(request,template,context)

def credencial_fisica(request):
    template = "home/credenciales/credencial_fisica.html"
    users = User.objects.all().exclude(is_active = "False")
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
        
    paginator = Paginator(users, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

    context = {'users': page_obj,'page_numbers': page_numbers}

    return render(request, template, context)

def ver(request, id):
    u = User.objects.get(id = id)
    user = User.objects.all().filter(id = id)
    inf = Information.objects.get(user_id = u)
    # mejorar este if
    if inf.departamento == "Agua":
        template = "home/credenciales/agua.html"
    elif inf.departamento == "Aire":
        template = "home/credenciales/aire.html"
    elif inf.departamento == "Dabba":
        template = "home/credenciales/dabba.html"
    elif inf.departamento == "Ether":
        template = "home/credenciales/ether.html"
    elif inf.departamento == "Fuego":
        template = "home/credenciales/fuego.html"
    elif inf.departamento == "Ignis":
        template = "home/credenciales/ignis.html"
    elif inf.departamento == "Digimundo":
        template = "home/credenciales/digimundo.html"
    elif inf.departamento == "Tierra":
        template = "home/credenciales/tierra.html"
    
    context = {"u": user}
    return render(request, template, context)
#documentos generados
def cartas(request):
    template = 'home/cartas/docs.html'
    users = User.objects.all().exclude(is_active = "False")
    
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
        Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
        Q(first_name__icontains=search_query) |  # Buscar en el nombre de pila
        Q(last_name__icontains=search_query) |  # Buscar en el apellido
        Q(information__departamento__icontains=search_query)  # Buscar en el departamento
)
    
    paginator = Paginator(users, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]
    
    context = {'users': page_obj,'page_numbers': page_numbers}
    
    return render(request, template, context)

def constancia (request, username=None):
    user = username
    us1= User.objects.get(username=user)
    template = 'home/cartas/constancia.html'
    context = {'us1':us1}
    
    return render(request, template, context)

def renuncia (request, username=None):
    user = username
    us1= User.objects.get(username=user)
    template = 'home/cartas/renuncia.html'
    context = {'us1':us1}
    
    return render(request, template, context)

def finiquito (request, username=None):
    user = username
    us1= User.objects.get(username=user)
    template = 'home/cartas/finiquito.html'
    context = {'us1':us1}
    
    return render(request, template, context)


@login_required
def kaisen(request):
    template = 'home/kaizen.html'
    users = User.objects.all().exclude(is_active = "False")
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]


    context = {'users': page_obj, 'page_numbers': page_numbers}
    return render(request, template, context)

def perfilkaisen(request, username=None):
    template = 'home/perfilkaisen.html'
    user = User.objects.get(username=username)
    asignados = AsignacionHat.objects.filter(user_id=user.id)
    
    
    context =  {'user': user,'registros' : asignados}
    
    return render(request, template, context)

def uploadkaisen(request ,username=None):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        # Saving the information in the database
        kaisen = models.Kaisen(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid
            
        )
        kaisen.save()
        return redirect('perfilkaisen', username=username)

def psicologico(request):
    template = 'home/psicologico.html'
    users = User.objects.all().exclude(is_active = "False")
    documents = Document.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

    context = {"files": documents, 'users': page_obj, 'page_numbers': page_numbers}
    
    return render(request, template, context)

def perfilpsico(request, username=None):
    template = 'home/perfilpsico.html'
    user = User.objects.get(username=username)
    perfiles = Document.objects.filter(user_id=user.id)
    context =  {'user': user,'perfiles': perfiles}
    return render(request, template, context)

def uploadpsico(request, username=None):
    if request.method == "POST":
        
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid
        )
        document.save()
        return redirect('perfilpsico', username=username)

def medicos(request):
    template = 'home/medico.html'
    users = User.objects.all().exclude(is_active = "False")

    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]


    context = {'users': page_obj, 'page_numbers': page_numbers}
    return render(request, template, context)

def perfilmedico(request, username=None):
    template = 'home/perfilmedico.html'
    user = User.objects.get(username=username)
    justificantes = Justificantesmedicos.objects.filter(user_id=user.id)
    context =  {'user': user,'justificantes':justificantes}
    return render(request, template, context)

def uploadmedicjust(request, username=None):
    if request.method == "POST":
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        justificant = models.Justificantesmedicos(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid    
        )
        justificant.save()
        return redirect('perfilmedico', username=username)

def organigrama(request):
    template = 'home/organigrama.html'
    users = User.objects.all().exclude(is_active = "False")

    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]


    context = {'users': page_obj, 'page_numbers': page_numbers}
    return render(request, template, context)
#por configurar

def perfillegal(request, id=None):
    user_id2=id
    template = 'social/perfillegal.html'
    registros = AsignacionHat.objects.filter(user_id=user_id2) #variable para comparar el hat de la cuenta
    users = User.objects.all().exclude(is_active = "False") #obtiene todos los usuarios
    tiene_permiso = registros.filter(hat_id__in=[42, 22]).exists()
    legals = Documentoslegales.objects.all() 
    documentoP = documentacion.objects.all()
    
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]
    context = {"legalfiles": legals, 'users': page_obj,"documentoP": documentoP,'registros':registros, 'page_numbers': page_numbers, 'tiene_permiso': tiene_permiso, "userid": user_id2}
    
    return render(request, template, context) 

#Files Medicos
def medicfiles(request, username=None):
    template = 'social/medicfiles.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, {'user': user, 'posts': posts})


#Justificantes Files
def justifyfiles(request, username=None):
    template = 'social/justifyfiles.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, {'user': user, 'posts': posts})

    
def viewfiles(request, username=None):
    template = 'social/viewfiles.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
        documents = models.Document.objects.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, { 'files': documents, 'user': user, 'posts': posts})  

#Files Legales
def legalfiles(request, username=None):
    template = 'social/legalfiles.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, {'user': user, 'posts': posts})

#Subir archivos a perfil Psicologico


def legalDocumentos(request, username=None):
    template = 'social/legalDocumentos.html'
    documentoP = documentacion.objects.all()
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user

    context = {'user': user, 'documentoP': documentoP}
    return render(request, template, context)

def subirdocumentacion(request):
    users = User.objects.all().exclude(is_active = "False")
    legals = Documentoslegales.objects.all()
    documentoP = documentacion.objects.all()
    registros = AsignacionHat.objects.all()
    hat = Hat.objects.order_by('id')
    if request.method == "POST":
        # Fetching the form data
        TipoDocumento = request.POST["TipoDocumento"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["userid"]
        # Saving the information in the database
        documento1 = models.documentacion(
            TipoDocumento = TipoDocumento,
            uploadedFile = uploadedFile,
            user_id = userid,
            
        )
        documento1.save()
        context = {'users': users, 'legals' : legals, 'documentoP': documentoP,'registros':registros,'hat':hat}
    return render(request, 'social/perfillegal.html', context)

def inclusiondocumentos(request, username=None):
    template = 'social/inclusiondocumentos.html'
    documentoP = documentacion.objects.all()
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user

    context = {'user': user, 'documentoP': documentoP}
    return render(request, template, context)

def subirinclusion(request):
    users = User.objects.all().exclude(is_active = "False")
    legals = Documentoslegales.objects.all()
    documentoP = documentacion.objects.all()
    registros = AsignacionHat.objects.all()
    hat = Hat.objects.order_by('id')
    if request.method == "POST":
        # Fetching the form data
        TipoDocumento = request.POST["TipoDocumento"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["userid"]
        # Saving the information in the database
        documento1 = models.documentacion(
            TipoDocumento = TipoDocumento,
            uploadedFile = uploadedFile,
            user_id = userid,
            
        )
        documento1.save()
         # En lugar de redirigir, envía una respuesta JSON de éxito
        response_data = {'success': True}
        return JsonResponse(response_data)
    

#Subir archivos A Perfil Medico
def uploadmedic(request, username=None):
    template = 'social/perfilmedico.html'
    users = User.objects.all().exclude(is_active = "False")
    if request.method == "POST":
        
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        # Saving the information in the database
        medic = models.Documentosmedicos(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid
            
        )
        medic.save()

    medics = models.Documentosmedicos.objects.all()
    return render(request, template, {
        "medicfiles": medics, 'users': users })


#Subir archivos a perfil legal
def uploadlegal(request, username=None):
    template = 'social/perfillegal.html'
    users = User.objects.all().exclude(is_active = "False")
    if request.method == "POST":
        
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        # Saving the information in the database
        legal = models.Documentoslegales(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid
            
        )
        legal.save()

    legals = models.Documentoslegales.objects.all()
    return render(request, template, {
        "legalfiles": legals, 'users': users })

#notificaciones

    
    