from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Produtos


def index(request):

    produtos = Produtos.objects.all()
    
    context = {
        'curso': 'Programação web',
        'instrutor': 'Renato Oliveira',
        'produtos' : produtos

    }
    return render(request, "index.html", context=context)

def contato(request):
    return render(request, "contato.html")

def produto(request, pk):
    
    item = Produtos.objects.get(id=pk)
    context = {
        'produto': item
    }
    
    return render(request,"produto.html", context=context)