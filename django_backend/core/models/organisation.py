from django.db import models
from django.utils.translation import gettext_lazy as _

from .customuser import CustomUser



class Organisation(models.Model):
    ispublic = models.BooleanField(default=True)     # Public organisation yes or no?
    name = models.CharField(max_length=255, unique=False, blank=False)
    description = models.TextField(max_length=1000)
    # image = models.ImageField(blank=True, upload_to="organisation/", default="organisation/default.png")
    creator = models.ForeignKey('CustomUser', null=True, blank=True, default= None, editable=False, related_name='organisation_creator', on_delete=models.SET_DEFAULT) # change to foreignkey
    participants = models.ManyToManyField(to='CustomUser', through='UserOrganisation', related_name='accessible_organisations')
    title = models.CharField(max_length=250)
    content = models.TextField()
    

    class Meta:
        verbose_name = _('organisation')
        verbose_name_plural = _('organisations')


    def __str__(self):
        return self.name

    # o1.userorganisation_set.all() & o1.participants.all()
    # u1.userorganisation_set.all() & u1.accessible_organisations.all()