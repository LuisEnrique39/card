from django.urls import path, re_path
from django.conf.urls import url
from apps.cliente import views

urlpatterns = [

    # Solicitar
    path('peticiones/', views.peticiones, name='peticiones'),
    path("information/<int:id>/",views.information, name="information"),
    path("update/<int:id>/", views.update, name='update'),
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    #puestos
]
