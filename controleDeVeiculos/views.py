from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
# Create your views here.


from .models import Controle, Veiculo

from .forms import MotoristaForm, VeiculoForm, ControleForm


oleo = False
edit = False
cad = False
veiculo = False


def reset():
    global oleo
    oleo = False

    global cad
    cad = False

    global edit
    edit = False

    global veiculo
    veiculo = False


def setOleoTrue():
    global oleo
    oleo = True


def setEditTrue():
    global edit
    edit = True


def setCadTrue():
    global cad
    cad = True


def setVeiculo(veic):
    global veiculo
    veiculo = veic


def index(request):
    controles = Controle.objects.all().order_by('-data_saida')
    if request.method == 'POST':
        dates = request.POST.get('date')
        if dates != '':
            dates = datetime.strptime(dates, '%Y-%m-%d').date()
            controles = Controle.objects.all().filter(
                data_saida=dates).order_by('-data_saida')

    return render(request, 'index.html', {'controles': controles, 'oleo': oleo, 'edit': edit, 'cad': cad, 'veiculo': veiculo})


def veiculos(request):
    reset()
    formulario = VeiculoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Veiculo cadastrado com sucesso')
    return render(request, 'veiculos/form.html', {'formulario': formulario})


def motorista(request):
    reset()
    formulario = MotoristaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Motorista cadastrado com sucesso')
    return render(request, 'motorista/form.html', {'formulario': formulario})


def cadastrarControle(request):
    reset()
    formulario = ControleForm(request.POST or None)
    if formulario.is_valid() and request.POST:
        formulario.save()
        km = float(request.POST.get('km_retorno'))
        cod_veic = request.POST.get('cod_veiculos')
        veiculo = Veiculo.objects.get(id=cod_veic)

        if(km >= veiculo.km_troca_oleo):
            setOleoTrue()
        setVeiculo(veiculo)
        setCadTrue()
        return redirect('index')
    return render(request, 'criarControle.html', {'formulario': formulario})


def visualizarControle(request, id):
    reset()
    controle = Controle.objects.get(id=id)
    formulario = ControleForm(request.POST or None, instance=controle)
    return render(request, 'visualizarControle.html', {'formulario': formulario, 'view': True})


def editarControle(request, id):
    reset()
    controle = Controle.objects.get(id=id)
    veiculo = Veiculo.objects.get(id=controle.cod_veiculos.id)
    formulario = ControleForm(request.POST or None, instance=controle)
    if formulario.is_valid() and request.POST:
        formulario.save()
        if(controle.km_retorno >= veiculo.km_troca_oleo):
            setOleoTrue()
        setEditTrue()
        setVeiculo(veiculo)
        return redirect('index')
    return render(request, 'editarControle.html', {'formulario': formulario})


def excluirControle(request, id):
    reset()
    controle = Controle.objects.get(id=id)
    if request.method == 'POST':
        controle.delete()
        return redirect('index')
    return render(request, 'excluirControle.html')
