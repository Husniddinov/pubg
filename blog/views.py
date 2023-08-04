from django.shortcuts import render, redirect, reverse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import random
# Create your views here

# Create your views here.


def index(request):
    posts = Post.objects.all()[:3]
    return render(request, 'blog/index.html')

def video(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/video.html')
    

def videos(request):
    posts = Post.objects.filter(publish = 1).order_by('-date')

def add_video(request):
    if request.method == "POST":
        post = Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('index')
    return render(request, 'blog/add_post.html')   


     
def delete_video(request, id):
    if request.method == "VIDEO":
        post = Post.objects.get(id=id)
        post.delete()
    return redirect('index')


@csrf_exempt
def like(request, slug):
    post = Post.objects.get(slug_exact=slug)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if not post.like_set.filter(user = request.user).exists():
                post.like_set.create(user = request.user)
                if post.dislike_set.filter(user = request.user).exists():
                    dislike = request.user.dislike_set.get(post = post)
                    dislike.delete()
        return HttpResponse('hi')
    
@csrf_exempt
def dislike(request, slug):
    post = Post.objects.get(slug_exact=slug)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if not post.dislike_set.filter(user = request.user).exists():
                post.dislike_set.create(user = request.user)
                if post.like_set.filter(user = request.user).exists():
                    like = request.user.like_set.get(post = post)
                    like.delete()
            return HttpResponse('hi')
        
def comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        comment = post.comment_set.create(
            author = request.user,
            text = request.POST.get('text')
        )
        if request.user.is_superuser:
            comment.publish = True
            comment.save()
    return redirect(reverse('post_detail_url', kwargs={'id': id}))
        
def comment_delete(request, id , pk):
     post = Post.objects.get(slug_exact = id)
     comment = post.comment_set.get(id = pk)
     if request.method == 'POST':
        comment.delete()
        return redirect(reverse('index', kwargs={'id':id}))
     
def add_post(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.video = request.POST.get('video')
        post.save()
        return redirect('index')
    return render (request, 'blog/add_post.html')

def delate_post (request, id):
    if request.method == 'POST':
        post = Post.objects.get(id = id)
        post.delete()
    return redirect ('index')
