from django.contrib import admin
from import_export import resources
from .models import Post, Profile, Relationship,Information
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.

admin.site.register(Relationship)

@admin.register(Profile)
class FotoAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id', 'user')
    list_filter = ('id','user')

class PostResource(resources.ModelResource): 
 
    class Meta:
        model = Post
        fields = ('fullname','timestamp','content','status','Fecha','entrada')
        exclude = ('activate', )
        export_order = ('fullname','timestamp','content','status','Fecha','entrada')

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource
    """Profile model admin."""

    list_display = ('user','timestamp','content','status','activate','Fecha','entrada')
    list_filter = (('timestamp',DateRangeFilter),('timestamp',DateTimeRangeFilter),'user','content')

class InfoResource(resources.ModelResource): 
 
    class Meta:
        model = Information
        fields = ('id','first_name','last_name','telefono','telefono_casa','nacimiento','direccion','contacto_emergencia','telefono_emergencia','puesto','departamento',)
        exclude = ('is_leader')
        export_order = ('id','first_name','last_name','telefono','telefono_casa','nacimiento','direccion','contacto_emergencia','telefono_emergencia','puesto','departamento',)


@admin.register(Information)
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = InfoResource
    """Profile model admin."""

    list_display = ('id','first_name','last_name','telefono','telefono_casa','nacimiento','direccion','contacto_emergencia','telefono_emergencia','puesto','departamento','is_leader')
    list_filter = ('first_name','departamento','is_leader')
