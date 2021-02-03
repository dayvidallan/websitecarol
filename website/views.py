from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Perfil


def blog(request):

    list_posts = Post.objects.filter(deleted=False)

    meu_perfil = Perfil.objects.all()

    data = {
            'posts': list_posts,
            'perfil': meu_perfil,
            }

    return render(request, 'index.html', data)


def post_detail(request, id):

    post = Post.objects.get(id=id)

    meu_perfil = Perfil.objects.all()

    data = {
        'post': post,
        'perfil': meu_perfil,
    }
    return render(request, 'post_detail.html', data)


