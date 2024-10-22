from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.template import loader
from .models import Post

def home(request):
    all_posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': all_posts})

def post(request, id):
    valid_id = False
    all_posts = Post.objects.all()
    for post in all_posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        return render(request, 'posts/post.html', {'post_dict': post_dict})
    else:
        raise Http404()