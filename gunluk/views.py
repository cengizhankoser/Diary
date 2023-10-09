from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import GunlukOlusturForm
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
def anasayfa(request):
    # Burada ana sayfanın içeriğini oluşturabilirsiniz
    return render(request, 'anasayfa.html')
    
def gunluk_olustur(request):    
    if request.method == 'POST':
        form = GunlukOlusturForm(request.POST)
        if form.is_valid():
            gunluk = form.save(commit=False)
            gunluk.kullanici = request.user  # Günlüğü oturum açmış kullanıcıya atayın
            gunluk.save()
            return redirect('anasayfa')  # Günlük oluşturulduktan sonra yönlendirme
    else:
        form = GunlukOlusturForm()
    return render(request, 'gunluk/gunluk_olustur.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

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
