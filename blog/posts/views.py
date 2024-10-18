from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return HttpResponse("Hello World!")

def post(request, id):
    return HttpResponse(id)

def google(request):
    return HttpResponseRedirect('https://www.google.com')