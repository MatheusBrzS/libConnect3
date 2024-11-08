from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.utils.timezone import now
from django.utils import timezone

from main.forms.ReservaForm import ReservaForm
from main.models import Emprestimo
from main.models import Livro

class ReservaConfirmacaoView(CreateView):
    model = Emprestimo
    form_class = ReservaForm
    template_name = 'reserva-confirmacao.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        livro = get_object_or_404(Livro, pk=self.kwargs['pk'])
        context['today'] = timezone.now()
        context['livro'] = livro
        return context

    def form_valid(self, form):
        livro = get_object_or_404(Livro, pk=self.kwargs['pk'])
        emprestimo = form.save(commit=False)
        emprestimo.livro = livro
        emprestimo.usuario = self.request.user
        emprestimo.data_emprestimo = now() 
        emprestimo.status = 'Pendente'
        emprestimo.save()
        return redirect('reserva_sucesso')