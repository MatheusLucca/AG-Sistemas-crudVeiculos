from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('veiculos', views.veiculos, name='veiculos'),
    path('motorista', views.motorista, name='motorista'),

]
