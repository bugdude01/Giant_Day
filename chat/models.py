from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.urls import reverse


# class Topic(models.Model):
#    title = models.CharField(max_length=200)
#    author = models.ForeignKey(User, on_delete=models.CASCADE)
#    body = models.TextField()
#    started = models.DateTimeField(auto_now_add=True)
#
#    def __str__(self):
#        return self.title


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chat:all')
