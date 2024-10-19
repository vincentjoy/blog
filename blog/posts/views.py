from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    return render(request, 'posts/home.html', {'posts': posts})

def post(request, id):
    return HttpResponse(id)

def google(request):
    return HttpResponseRedirect('https://www.google.com')