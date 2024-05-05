import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fotografia(models.Model):
    CATEGORIA_CHOICES = [
        ('NEBULOSA', 'NEBULOSA'),
        ('ESTRELA', 'ESTRELA'),
        ('GALÁXIA', 'GALÁXIA'),
        ('PLANETA', 'PLANETA'),
    ]

    nome = models.CharField(max_length=255, verbose_name='Nome')
    legenda = models.CharField(max_length=255, verbose_name='Legenda')
    categoria = models.CharField(max_length=255, choices=CATEGORIA_CHOICES, default='', verbose_name='Categoria')
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição')
    imagem = models.ImageField(upload_to='fotografias/%Y/%m/%d/', null=True, blank=True, verbose_name='Fotografia')
    status = models.BooleanField(default=True, verbose_name='Publicado')
    data_fotografia = models.DateTimeField(default=datetime.datetime.now, verbose_name='Data da Fotografia')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuário')

    def __str__(self):
        return self.nome