
from django.db import models
from django.contrib.auth.models import User
#admins
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    codigo_postal = models.IntegerField(blank=True, null=True)
    numero = models.CharField(max_length=100, blank=True)
    about_me = models.TextField(blank=True)
    foto_de_perfil = models.ImageField(upload_to='assets/img/perfil/', blank=True, null=True)


    def __str__(self):
        return self.user.username



class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre



TIPO_DOC = (
    ('INE','INE'),
    ('Contrato','Contrato'),
    ('NDA', 'NDA'),
    ('Reglamento', 'Reglamento'),
    ('Priv datos', 'Priv datos'),
    ('Domicilio', 'Reglamento'),
    ('Acta nacimiento', 'Acta nacimiento')
)

class Kaisen(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='actas', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Actas Kaisen/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'kaizen'
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']


class Document(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='files', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Archivos Psicologicos/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Documentos Psicologicos'

        
        
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']

class Documentosmedicos(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='medicfiles', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Archivos Medicos/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Documentos Medicos'

    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']

class Justificantesmedicos(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='justifyfiles', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Justificantes Medicos/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Justificantes Medicos'
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']

DOCUMENTOS = (
    ('INE','INE'),
    ('Contratos','Contratos'),
    ('Prestaciones', 'Prestaciones'),
    ('NDA', 'NDA'),
    ('Reglamento', 'Reglamento'),
    ('Priv Datos', 'Priv Datos'),
)
class Documentoslegales(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='legalfiles', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Archivos Legales/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Documentos Legales'
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload'] 
        
class Egresos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    ingreso = models.CharField(max_length=250, null=True)
    egreso = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name_plural = 'Salida empresa'

class Hat(models.Model):
    nombre_hat = models.CharField(max_length=500, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    class meta:
        verbose_name_plural = 'Hats'

class AsignacionHat(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='hats', null=True)
    hat = models.ForeignKey(
        Hat, on_delete=models.CASCADE, related_name='hats', null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    class meta:
        verbose_name_plural = 'Asignacion de Hats'

class Actividades(models.Model):
    actividades = models.CharField(max_length=500, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    hat = models.ForeignKey(
        Hat, on_delete=models.CASCADE, related_name='actividades', null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

class TimestampedItem(models.Model):
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

class documentacion(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='documentfiles', null=True)
    TipoDocumento = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Documentos Personales/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Documentos Personales'
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']

class CredentialToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    token = models.CharField(max_length=250, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

class contratacion(models.Model):
    NombreAspirante = models.CharField(max_length = 200)
    uploadedNotes = models.FileField(upload_to = "Notas/")
    uploadedCV = models.FileField(upload_to = "CV/")
    is_contratado = models.BooleanField(default=False,null=True)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    comentarios = models.CharField(max_length = 200,null=True)
    
    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Documentos contratacion'
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']