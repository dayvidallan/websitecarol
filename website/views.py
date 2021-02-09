from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


from .models import Post, Perfil, Contact


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

    return render(request, 'post_detail.html', {'post': post})





def save_form(request):
    name = request.POST['name']
    Contact.objects.create(
        name=name,
        nrTelCelular=request.POST['fone'],
        email=request.POST['email'],
        message=request.POST['message'],

    )

    return render(request, 'contact_sucess.html', {'name_contact': name})
