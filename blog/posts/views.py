from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.template import loader
from .models import Post

def home(request):
    all_posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': all_posts})

def post(request, id):
    try:
        post = Post.objects.get(id=id)
        return render(request, 'posts/post.html', {'post_dict': post})
    except:
        raise Http404()