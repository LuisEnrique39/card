from django import forms
from .models import UserInfo

class PerfilForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['foto_de_perfil']

