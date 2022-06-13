from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
# Create your views here.


from .models import Controle, Veiculo

from .forms import MotoristaForm, VeiculoForm, ControleForm


def index(request):
    controles = Controle.objects.all().order_by('-data_saida')
    if request.method == 'POST':
        dates = request.POST.get('date')
        if dates != '':
            dates = datetime.strptime(dates, '%Y-%m-%d').date()
            controles = Controle.objects.all().filter(
                data_saida=dates).order_by('-data_saida')

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
    formulario = ControleForm(request.POST or None)
    oleo = False
    veiculo = False
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, 'Controle cadastrado com sucesso')
        km = float(request.POST.get('km_retorno'))
        cod_veic = request.POST.get('cod_veiculos')
        veiculo = Veiculo.objects.get(id=cod_veic)

        if(km >= veiculo.km_troca_oleo):
            oleo = True
    return render(request, 'criarControle.html', {'formulario': formulario, 'oleo': oleo, 'veiculo': veiculo})


def visualizarControle(request, id):
    controle = Controle.objects.get(id=id)
    formulario = ControleForm(request.POST or None, instance=controle)
    return render(request, 'visualizarControle.html', {'formulario': formulario, 'view': True})


def editarControle(request, id):
    controle = Controle.objects.get(id=id)
    veiculo = Veiculo.objects.get(id=controle.cod_veiculos.id)
    formulario = ControleForm(request.POST or None, instance=controle)
    oleo = False
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, 'Controle editado com sucesso')
        if(controle.km_retorno >= veiculo.km_troca_oleo):
            oleo = True
    return render(request, 'editarControle.html', {'formulario': formulario, 'oleo': oleo, 'veiculo': veiculo})


def excluirControle(request, id):
    controle = Controle.objects.get(id=id)
    controle.delete()
    return redirect('index')
