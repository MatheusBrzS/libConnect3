from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from main.views import (
    IndexTemplateView,
    LivroDetailView,
    ReservaConfirmacaoView,
)

app_name = 'main'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro-detail'),
    path('default/', TemplateView.as_view(template_name="default.html"), name='default'),
    path('reserva/', TemplateView.as_view(template_name="reserva.html"), name='reserva'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro-detalhes'),
    path('reserva/<int:pk>/confirmacao/', ReservaConfirmacaoView.as_view(), name='reserva-confirmacao'),
    path('reserva-sucesso/', TemplateView.as_view(template_name="reserva-sucesso.html"), name='reserva-sucesso'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

