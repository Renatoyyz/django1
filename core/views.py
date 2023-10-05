from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

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
    
    # item = Produtos.objects.get(id=pk)
    item = get_object_or_404(Produtos, id=pk)
    context = {
        'produto': item
    }
    
    return render(request,"produto.html", context=context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)