from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            homeurl = reverse('home')
            return HttpResponseRedirect(homeurl)
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })

def auth_login(request):
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
