from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from main.models.Livro import Livro

class LivroDetailView(LoginRequiredMixin, DetailView):
    model = Livro
    template_name = 'livro-detail-view.html'
    context_object_name = 'livro'