from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import TemplateView
from main.views import (
    IndexTemplateView,
    LivroDetailView,
)

app_name = 'main'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro-detail'),
    path('default/', TemplateView.as_view(template_name="default.html"), name='default'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
