from django.db import models
from main.models.Livro import Livro
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('Pendente', 'Pendente'),
    ('Aprovado', 'Aprovado'),
]

class Reserva(models.Model):
    data_reserva = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f'Reserva de {self.livro.titulo} por {self.usuario.username}'