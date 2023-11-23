
from django.urls import path, re_path
from django.conf.urls import url
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    #profile
    path('profileg/<str:username>/', views.profileg, name='profileg'),

    #esto es de asignar vacaciones
    path('asignar_vacaciones/<int:user_id>/', views.asignar_vacaciones, name='asignar_vacaciones'),
    path('asignar_vacacionespdf/<int:user_id>/', views.asignar_vacacionespdf, name='asignar_vacacionespdf'),
    path('CONTRATO_INDIVIDUALpdf/<int:user_id>/', views.contratos, name='CONTRATO_INDIVIDUALpdf'),


    path('asignarhat/<int:user_id>/', views.asignarhat, name='asignarhat'),
    path('asignaregreso/<int:user_id>/', views.asignaregreso, name='asignaregreso'),
    path('eliminar_foto/', views.eliminar_foto, name='eliminar_foto'),
    #generacion de qrs
    path('qr/<int:user_id>/', views.generar_codigo_qr, name='generar_codigo_qr'),
    path('credencial/<str:tokenid>/', views.credencial, name='credencial'),
    #menu
    url(r'^perfil_general/$', views.perfil_general, name='perfil_general'),
    url(r'^asistencia/$', views.asistencia, name='asistencia'),
    #credenciales fisicas
    url('credencial_fisica/',views.credencial_fisica, name='credencial_fisica'),
    path("ver/<int:id>",views.ver, name="ver"),
    #documentos
    url(r'^cartas/$', views.cartas, name='cartas'),
    path('constancia/<str:username>/', views.constancia, name='constancia'),
    path('renuncia/<str:username>/', views.renuncia, name='renuncia'),
    path('finiquito/<str:username>/', views.finiquito, name='finiquito'),

    url(r'^kaisen/$', views.kaisen, name='kaisen'),
    path('perfilkaisen/<str:username>/', views.perfilkaisen, name='perfilkaisen'),
    path(r'^uploadkaisen/<str:username>/', views.uploadkaisen, name='uploadkaisen'),

    url(r'^psicologico/$', views.psicologico, name='psicologico'),
    path('psicologico/<str:username>/', views.perfilpsico, name='perfilpsico'),
    path(r'^uploadpsico/<str:username>/', views.uploadpsico, name='uploadpsico'),

    url(r'^medicos/$', views.medicos, name='medicos'),
    path('perfilmedico/<str:username>/', views.perfilmedico, name='perfilmedico'),
    path(r'^uploadmedicjust/<str:username>/', views.uploadmedicjust, name='uploadmedicjust'),

    url(r'^organigrama/$', views.organigrama, name='organigrama'),
]
