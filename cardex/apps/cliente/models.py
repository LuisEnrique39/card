from django.db import models
from django.contrib.auth.models import User
from apps.home.models import Proyecto 
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
#cliente
class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)  # Agrega esta referencia
    mensaje = models.CharField(max_length=255)
    leida = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensaje

ENTRADAS_SALIDAS = (
    ('entrada oficina','ENTRADA OFICINA'),
    ('entrada homeofice','ENTRADA HOMEOFICE'),
    ('salida oficina', 'SALIDA OFICINA'),
    ('salida homeofice', 'SALIDA HOMEOFICE')
)

RETCA = (
    ('A Tiempo','A Tiempo'),
    ('Retardo','Retardo')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='batman.png')
    
    def __str__(self):
            return f'Foto de perfil de { self.user.information.first_name } { self.user.information.last_name }'

    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
            .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
            .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(choices=ENTRADAS_SALIDAS)
    activate = models.BooleanField(default=True,null=True)
    fullname = models.CharField(max_length = 200,null=True)
    status = models.TextField(choices=RETCA,default=True,null=True)
    Fecha = models.CharField(max_length = 200,null=True)
    entrada = models.CharField(max_length = 200,null=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'Entradas/Salidas' 
    
    def clean_renewal_date(self):
        data = self.full_clean['timestamp']
    
    class MyModelAdmin(admin.ModelAdmin):
        list_display = ('datetime')

    class MyModel(models.Model):
        datetime = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")


class Relationship(models.Model):
    from_user = models.ForeignKey(
        User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'

    class Meta:

        verbose_name_plural = 'Relaciones'
        indexes = [
            models.Index(fields=['from_user', 'to_user', ]),
        ]


class Information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    telefono = models.CharField(max_length=250, null=True, unique=False)
    telefono_casa = models.CharField(max_length=250, null=True,  unique=False)
    nacimiento = models.CharField(max_length=250, null=True)
    direccion = models.CharField(max_length=300, null=True)
    contacto_emergencia = models.CharField(max_length=250, null=True)
    telefono_emergencia = models.CharField(max_length=250, null=True)
    puesto = models.CharField(max_length=250, null=True)
    departamento = models.CharField(max_length=250, null=True)
    is_leader = models.BooleanField(default=False,null=True)

    class Meta:
        verbose_name_plural = 'Informacion Personal'

class DatosMedicos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    edad = models.CharField(max_length=250, null=True)
    peso = models.CharField(max_length=250, null=True)
    estatura = models.CharField(max_length=250, null=True)
    alergias = models.CharField(max_length=500, null=True)
    sangre = models.CharField(max_length=250, null=True)
    enfermedad = models.CharField(max_length=300, null=True)
    lentes = models.CharField(max_length=250, null=True)
    fumas = models.CharField(max_length=250, null=True)
    tomas = models.CharField(max_length=250, null=True)
    deporte = models.CharField(max_length=250, null=True)
    sueño = models.CharField(max_length=250, null=True)
    covid = models.CharField(max_length=250, null=True)
    vacuna = models.CharField(max_length=250, null=True)
    
