from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


from .models import Controle

from .forms import MotoristaForm, VeiculoForm, ControleForm


def index(request):
    controles = Controle.objects.all()
    return render(request, 'index.html', {'controles': controles})


def veiculos(request):
    formulario = VeiculoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Veiculo cadastrado com sucesso')
    return render(request, 'veiculos/form.html', {'formulario': formulario})


def motorista(request):
    formulario = MotoristaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Motorista cadastrado com sucesso')
    return render(request, 'motorista/form.html', {'formulario': formulario})


def cadastrarControle(request):
    return render(request, 'criarControle.html')


def visualizarControle(request, id):
    controle = Controle.objects.get(id=id)
    formulario = ControleForm(request.POST or None, instance=controle)
    return render(request, 'visualizarControle.html', {'formulario': formulario, 'view': True})


def editarControle(request, id):
    controle = Controle.objects.get(id=id)
    formulario = ControleForm(request.POST or None, instance=controle)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    return render(request, 'editarControle.html', {'formulario': formulario})


def excluirControle(request, id):
    controle = Controle.objects.get(id=id)
    controle.delete()
    return redirect('index')
