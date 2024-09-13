from django.urls import path, include
from main.views import (
    IndexTemplateView,
    LivroDetailView,
)

app_name = 'main'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro-detail'),
]