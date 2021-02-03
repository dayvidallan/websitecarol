from django.contrib import admin
from .models import Post, Perfil, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title']
    search_fields = ['title', 'sub_title']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)

    #def get_queryset(self, request):
        #return Post.objects.filter(deleted=False)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['name', 'especialidade', 'nrTelCelular', 'texto']
    search_fields = ['name', 'especialidade', 'nrTelCelular', 'texto']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'nrTelCelular']
    search_fields = ['name', 'email', 'nrTelCelular']

admin.site.register(Post, PostAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Contact, ContactAdmin)


