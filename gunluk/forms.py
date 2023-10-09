from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Gunluk  # Gunluk modelini kullanıyoruz models.py'dan


class KayitForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

class GunlukOlusturForm(forms.ModelForm):
    class Meta:
        model = Gunluk  # Kullanılacak model
        fields = ['baslik', 'icerik']  # Kullanıcıdan alınacak alanlar
