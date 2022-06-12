from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Controle


def index(request):
    controles = Controle.objects.all()
    return render(request, 'index.html', {'controles': controles})


def veiculos(request):
    return render(request, 'veiculos/form.html')


def motorista(request):
    return render(request, 'motorista/form.html')


def cadastrarControle(request):
    return render(request, 'criarControle.html')


def editarControle(request):
    return render(request, 'editarControle.html')
