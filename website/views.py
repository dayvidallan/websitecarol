from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
    lista = [
        'Django', 'Python', 'git', 'Html'
    ]
    data = {'name': 'site_carol', 'lista_tecnologias': lista}
    return render(request, 'index.html', data)
