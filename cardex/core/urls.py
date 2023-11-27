
from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")), # Urls from home
    path("", include("apps.cliente.urls")), # Urls from cliente
]

