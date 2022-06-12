from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def veiculos(request):
    return render(request, 'veiculos/form.html')


def motorista(request):
    return render(request, 'motorista/form.html')
