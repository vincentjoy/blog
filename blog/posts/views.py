from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")

def post(request, id):
    return HttpResponse(id)