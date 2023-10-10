from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import GunlukOlusturForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Gunluk
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def kayit(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('anasayfa')
    else:
        form = UserCreationForm()
    return render(request, 'registration/kayit.html', {'form': form})
@login_required
def anasayfa(request):
    # Günlüğü veritabanından alış
    gunlukler = Gunluk.objects.filter(kullanici=request.user)
    context = {
        'gunlukler': gunlukler
    }
    return render(request, 'anasayfa.html', context)

@login_required
def gunluk_olustur(request):    
    if request.method == 'POST':
        form = GunlukOlusturForm(request.POST)
        if form.is_valid():
            gunluk = form.save(commit=False)
            gunluk.kullanici = request.user  # Günlüğü oturum açmış kullanıcıya atama
            gunluk.save()
            return redirect('anasayfa')  
    else:
        form = GunlukOlusturForm()
    return render(request, 'gunluk/gunluk_olustur.html', {'form': form})


def giris_yap(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('anasayfa')  # Kullanıcı giriş yaptıktan sonra yönlendirilecek sayfa
    else:
        form = AuthenticationForm()
    return render(request, 'registration/giris.html', {'form': form})

"""
@login_required
def gunluklerim(request):
    # Kullanıcının günlüklerini alın
    kullanici_gunlukler = Gunluk.objects.filter(kullanici=request.user)
    
    context = {
        'kullanici_gunlukler': kullanici_gunlukler
    }
    return render(request, 'gunluk/gunluklerim.html', context)

"""

@login_required
def gunluk_detay(request, gunluk_id):
    gunluk = get_object_or_404(Gunluk, pk=gunluk_id)
    return render(request, 'gunluk/gunluk_detay.html', {'gunluk': gunluk})
