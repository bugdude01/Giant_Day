from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Chat

# Create your views here.


def home(request):
    return render(request, 'chat/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'chat/signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['first_name'] + request.POST['last_name'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'chat/signup.html', {'error': 'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'chat/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'chat/login.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')


""" def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
 """
