from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import Controle

from .forms import MotoristaForm, VeiculoForm


def index(request):
    controles = Controle.objects.all()
    return render(request, 'index.html', {'controles': controles})


def veiculos(request):
    formulario = VeiculoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('veiculos')
    return render(request, 'veiculos/form.html', {'formulario': formulario})


def motorista(request):
    formulario = MotoristaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('motorista')
    return render(request, 'motorista/form.html', {'formulario': formulario})


def cadastrarControle(request):
    return render(request, 'criarControle.html')


def editarControle(request):
    return render(request, 'editarControle.html')


def excluirControle(request, id):
    controle = Controle.objects.get(id=id)
    controle.delete()
    return redirect('index')
