from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def blog(request):
    lista = [
        'Django', 'Python', 'git', 'Html'
    ]

    list_posts = Post.objects.filter(deleted=False)

    data = {'name': 'site_carol',
            'lista_tecnologias': lista,
            'posts': list_posts
            }

    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})


