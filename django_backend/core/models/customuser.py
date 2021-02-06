from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=75)
    first_name = models.CharField(max_length=50)
    last_name_prefix = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    registered_on = models.DateTimeField(default=now, editable=False)
    # organisations = models.ManyToManyField('Organisation', through='UserOrganisation')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        if not self.last_name_prefix:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.last_name_prefix} {self.last_name}"