from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from main.models.Livro import Livro

class LivroDetailView(DetailView):
    model = Livro
    template_name = 'livro-detail-view.html'
    context_object_name = 'livro'