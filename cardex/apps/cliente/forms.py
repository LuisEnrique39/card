from django import forms
from django.forms import widgets
from .models import Post
from django.contrib import admin


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['status', 'content', 'Fecha','entrada']
        
