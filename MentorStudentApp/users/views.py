from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *

def register(request):
    if request.method == 'POST':
        form = AppUserForm(request.POST)
        if form.is_valid():    
            form.save()
            messages.success(request, f'Registracija uspješna! Možete se prijaviti.')
            return redirect('login')
    else:
        form = AppUserForm()
    return render(request, 'users/register.html', { 'form': form })


def login(request):
    if request.method == 'POST':
        form = AppUserLogin(request.POST)
        if form.is_valid():    
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Welcome!')
            return redirect('Home')
    else:
        form = AppUserLogin()
    return render(request, 'users/login.html', {'form': form})
