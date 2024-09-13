from django.db import models
from main.models.Categoria import Categoria

STATUS_CHOICES = [
    ('Disponível', 'Disponível'),
    ('Indisponível', 'Indisponível'),
    ('Reservado', 'Reservado'),
]

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    isbn = models.CharField(max_length=13)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='livros')

    def __str__(self):
        return self.titulo