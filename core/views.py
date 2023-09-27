from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Programação web',
        'instrutor': 'Renato Oliveira'

    }
    return render(request, "index.html", context=context)

def contato(request):
    return render(request, "contato.html")