from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CreateUser
from django.views.generic import CreateView

# Create your views here.


class Signup(CreateView):
    form_class = CreateUser
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
