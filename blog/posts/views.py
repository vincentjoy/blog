from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def post(request, id):
    return HttpResponse(id)

def google(request):
    return HttpResponseRedirect('https://www.google.com')