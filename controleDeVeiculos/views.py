from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return HttpResponse("<h1> Bem vindo ao sistema de controle de veiculos </h1>")


def index(request):
    return render(request, 'index.html')
