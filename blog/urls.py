from django.urls import path
from . import views
from blog.models import Post


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.video, name='video'),
    path('post/', views.videos, name='videos'),
    path('crud/post/add-new', views.add_post, name= "logout"),
    path('crud/posts/<int:id>/delate', views.delate_post, name= "delate_post"),
    path('post/<int:id>/like/', views.like, name='like'),
    path('post/<int:id>/dislike/', views.dislike, name='dislike'),

]





