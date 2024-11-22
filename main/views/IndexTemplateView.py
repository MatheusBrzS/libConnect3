from typing import Any
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import Categoria
from main.models.Livro import Livro

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        livros = Livro.objects.all()

        categoriaId = self.request.GET.get('categoria')
        if categoriaId:
            livros = livros.filter(categoria__id=categoriaId)

        autor = self.request.GET.get('autor')
        if autor:
            livros = livros.filter(autor__icontains=autor)

        context['livros'] = livros
        context['categorias'] = Categoria.objects.all() 
        return context
