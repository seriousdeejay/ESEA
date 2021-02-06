from django.db import models
from .customuser import CustomUser


class Post(models.Model):
    owner = models.ManyToManyField(CustomUser, default=1)
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title