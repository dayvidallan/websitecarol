from django.urls import path, include
from .views import blog, post_detail, save_form

urlpatterns = [
    path('blog/', blog, name='home_blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('save-fom', save_form, name='save_form'),

]
