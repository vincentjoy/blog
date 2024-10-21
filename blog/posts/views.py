from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.template import loader

posts = [
    {
        "id":0,
        "title": "Post Title 1",
        "content": "Post 1 description"
    },
    {
        "id":1,
        "title": "Post Title 2",
        "content": "Post 2 description"
    },
    {
        "id":2,
        "title": "Post Title 3",
        "content": "Post 3 description"
    }
]

def home(request):
    return render(request, 'posts/index.html', {'posts': posts})

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        return render(request, 'posts/post.html', {'post_dict': post_dict})
    else:
        raise Http404()