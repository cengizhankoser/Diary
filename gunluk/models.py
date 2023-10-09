from django.db import models
from django.contrib.auth.models import User

class Gunluk(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.baslik
