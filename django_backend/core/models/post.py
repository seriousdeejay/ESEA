from django.db import models
from .customuser import CustomUser
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    # public = models.BooleanField      Public organisation yes or no?
    name = models.CharField(max_length=255, unique=False, blank=False)
    description = models.TextField(max_length=1000)
    # image = models.ImageField(blank=True, upload_to="organisation/", default="organisation/default.png")
    participants = models.ManyToManyField(to='CustomUser', through='UserOrganisation')
    #participant = models.CharField(max_length=50)
    # creator = models.ManyToManyField('CustomUser', default='', related_name='organisation_creator') # change to foreignkey
    title = models.CharField(max_length=250)
    content = models.TextField()
    

    class Meta:
        verbose_name = _('organisation')
        verbose_name_plural = _('organisations')


    def __str__(self):
        return self.title