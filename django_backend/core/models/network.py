from django.db import models
from django.utils.translation import gettext_lazy as _

from .customuser import CustomUser
from .organisation import Organisation


class Network(models.Model):
    ispublic = models.BooleanField(default=True)
    name = models.CharField(max_length=255, unique=False, blank=False)
    description = models.TextField(max_length=1000)
    # image = models.ImageField(blank=True, upload_to="network/", default="network/default.png")
    created_by = models.ForeignKey('CustomUser', null=True, blank=True, default=None, editable=False, related_name='network_creator', on_delete=models.SET_DEFAULT)
    organisations = models.ManyToManyField(Organisation, blank=True) 

    class Meta: 
        verbose_name = _('network')
        verbose_name_plural = _('networks')

    def __str__(self):
        return self.name