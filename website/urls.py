from django.urls import path, include
from .views import blog, post_detail

urlpatterns = [
    path('', blog, name='home_blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),

]
