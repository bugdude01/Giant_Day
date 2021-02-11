from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Topic


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        ]


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password1'
        ]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = (
            'title',
            'body',
        )
