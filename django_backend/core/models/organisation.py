from django.db import models
from django.utils.translation import gettext_lazy as _

from .user_organisation import UserOrganisation

class Organisation(models.Model):
    ispublic = models.BooleanField(default=True)
    name = models.CharField(max_length=255, unique=False, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    # image = models.ImageField(blank=True, upload_to="organisation/", default="organisation/default.png")
    created_by = models.ForeignKey('CustomUser', editable=False, on_delete=models.SET_NULL, null=True) # related_name='organisation_creator'
    members = models.ManyToManyField('CustomUser', through="UserOrganisation", through_fields=('organisation', 'user'), related_name='organisations', blank=True)

    class Meta:
        verbose_name = _('organisation')
        verbose_name_plural = _('organisations')

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

    def relevant_survey_responses(self):
        return UserOrganisation.objects.filter(organisation=self, survey_responses__isnull=False).distinct()