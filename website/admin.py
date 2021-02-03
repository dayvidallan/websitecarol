from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title']
    search_fields = ['title', 'sub_title']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)

    #def get_queryset(self, request):
        #return Post.objects.filter(deleted=False)



admin.site.register(Post, PostAdmin)

