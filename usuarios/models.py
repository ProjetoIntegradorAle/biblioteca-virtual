from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.username

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=400, blank=True)
    cidade = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    data_nascimento = models.DateField(null=True)
    telefone = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class FraseDoDia(models.Model):
    DIA_SEMANA_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    dia_semana = models.CharField(max_length=10, choices=DIA_SEMANA_CHOICES, unique=True)
    texto = models.TextField()
    autor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.dia_semana}: {self.texto} – {self.autor}"
