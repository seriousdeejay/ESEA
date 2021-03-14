from django.db import models
from django.utils.translation import gettext_lazy as _

from .customuser import CustomUser
from .user_organisation import UserOrganisation

class Organisation(models.Model):
    ispublic = models.BooleanField(default=True)
    name = models.CharField(max_length=255, unique=False, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    creator = models.ForeignKey('CustomUser', editable=False, on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(CustomUser, through="UserOrganisation", related_name='organisations', blank=True)
    def __str__(self):
        return self.name
# class organisationManager(models.Manager):
#     def create(self, request, name, description, ispublic=None):
#         organisation = self.create(ispublic=ispublic, name=name, description=description, creator=self.request.user)
#         return organisation

# #         return Response({"Nothing uploaded"})

# class Organisation(models.Model):
#     # objects = organisationManager()
#     ispublic = models.BooleanField(default=True)
#     name = models.CharField(max_length=255, unique=False, blank=False)
#     description = models.TextField(max_length=1000, blank=True)
#     # image = models.ImageField(blank=True, upload_to="organisation/", default="organisation/default.png")
#     creator = models.ForeignKey('CustomUser', editable=False, null=True, blank=True, default="None", related_name='organisation_creator', on_delete=models.SET_DEFAULT) # change to foreignkey
#     participants = models.ManyToManyField(to='CustomUser', through='UserOrganisation', related_name='accessible_organisations', blank=True)


#     class Meta:
#         verbose_name = _('organisation')
#         verbose_name_plural = _('organisations')


#     def __str__(self):
#         return self.name

#     def __repr__(self):
#         return self.name

    # o1.userorganisation_set.all() & o1.participants.all()
    # u1.userorganisation_set.all() & u1.accessible_organisations.all()