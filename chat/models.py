from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
