from django.db import models
from .customuser import CustomUser
from django.utils.translation import gettext_lazy as _


class Organisation(models.Model):
    # public = models.BooleanField      Public organisation yes or no?
    name = models.CharField(max_length=255, unique=False, blank=False)
    description = models.TextField(max_length=1000)
    # image = models.ImageField(blank=True, upload_to="organisation/", default="organisation/default.png")
    creator = models.ForeignKey('CustomUser', null=True, blank=True, default= None, related_name='organisation_creator', on_delete=models.SET_DEFAULT) # change to foreignkey
    participants = models.ManyToManyField(to='CustomUser', through='UserOrganisation')
    
    title = models.CharField(max_length=250)
    content = models.TextField()
    

    class Meta:
        verbose_name = _('organisation')
        verbose_name_plural = _('organisations')


    def __str__(self):
        return self.title