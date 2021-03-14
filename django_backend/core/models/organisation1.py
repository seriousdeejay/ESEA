from django.db import models

class Organisation(models.Model):
    ispublic = models.BooleanField(default=True)
    name = models.CharField(max_length=255, unique=False, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    creator = models.ForeignKey('CustomUser', editable=False, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name