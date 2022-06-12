from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('controle/cadastro', views.cadastrarControle, name='cadastrarControle'),
    path('veiculos', views.veiculos, name='veiculos'),
    path('motorista', views.motorista, name='motorista'),
    path('controle/edição', views.editarControle, name='editarControle')
]
