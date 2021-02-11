from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Chat, Topic
from .forms import CreateUserForm, LoginUserForm, TopicForm
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


def newchats(request):
    form = TopicForm(request.POST)

    if request.method == 'GET':
        return render(request, 'chat/startchat.html', {'form': form})

    else:
        form = TopicForm(request.POST)
        newtopic = form.save(commit=False)
        newtopic.user = request.user
        newtopic.save()
        return redirect('allchats')

    return render(request, 'chat/startchat.html', {'form': form})


def allchats(request):
    topics = Topic.objects.all()
    return render(request, 'chat/allchats.html', {'topics': topics})


def viewtopic(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk)
    return render(request, 'chat/viewtopic.html', {'topic': topic})
