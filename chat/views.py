from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Chat
from .forms import CreateUserForm, LoginUserForm
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'chat/home.html')


def signupuser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.sucess(request, 'Account created for ' + user)

    context = {'form': form}
    return render(request, 'chat/signup.html', context)


def loginuser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'chat/login.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
