from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. Site da BOSS boladona.")

def sobre(request):
    return render(request, 'sobre.html')

def diversidade(request):
    return HttpResponse("Guia Diversidade")

def sisters(request):
    return HttpResponse("Sisters")

def materiais(request):
    return HttpResponse("Materiais")

def inscricao(request):
    return HttpResponse("Inscreva-se")