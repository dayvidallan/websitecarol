from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    message = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title


class Perfil(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    especialidade = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    apresent = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    imagem = models.ImageField(upload_to='perfils', null=True, blank=True)

    def __str__(self):
        return self.texto




