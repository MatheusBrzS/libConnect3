from django.db import models
from main.models.Livro import Livro
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('Pendente', 'Pendente'),
    ('Aprovado', 'Aprovado'),
    ('Devolvido', 'Devolvido'),
]

class Emprestimo(models.Model):
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprestimos')

    def __str__(self):
        return f'{self.livro.titulo} emprestado por {self.usuario.username}'