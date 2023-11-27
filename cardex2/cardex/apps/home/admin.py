
from dataclasses import fields
from pyexpat import model
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Document, Documentosmedicos, Kaisen,Egresos, Justificantesmedicos, Documentoslegales, AsignacionHat, Hat, CredentialToken
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

@admin.register(Egresos)
class EgresoAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id', 'user','ingreso','egreso')
    list_filter = ('id','user')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')
    

#AdminMedico
@admin.register(Documentosmedicos)
class DocumentosmedicosAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')
    
#AdminJustificante
@admin.register(Justificantesmedicos)
class JustificantesmedicosAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')


#AdminKaisen
@admin.register(Kaisen)
class KaisenAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')

#AdminLegal
@admin.register(Documentoslegales)
class DocumentoslegalesAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')

@admin.register(AsignacionHat)
class AsignacionHat(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('create_at', 'hat_id', 'user_id')
    list_filter = ('id','user_id')

@admin.register(Hat)
class Hat(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id','nombre_hat')

@admin.register(CredentialToken)
class CredentialToken(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id','token', 'create_at','user_id')