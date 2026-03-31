from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.listar_filmes, name='listar_filmes'),
    path('filmes/bem-avaliados/', views.listar_filmes_bem_avaliados, name='filmes_bem_avaliados'),
]