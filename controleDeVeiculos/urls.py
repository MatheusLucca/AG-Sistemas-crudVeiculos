from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('controle/cadastro', views.cadastrarControle, name='cadastrarControle'),
    path('veiculos', views.veiculos, name='veiculos'),
    path('motorista', views.motorista, name='motorista'),
    path('controle/visualizar/<int:id>',
         views.visualizarControle, name='visualizar'),
    path('controle/editar/<int:id>', views.editarControle, name='editar'),
    path('controle/excluir/<int:id>', views.excluirControle, name='excluir'),

]
