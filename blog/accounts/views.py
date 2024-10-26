from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            homeurl = reverse('home')
            return HttpResponseRedirect(homeurl)
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })
