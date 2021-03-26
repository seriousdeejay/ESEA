from django.db import models
from django.utils.translation import gettext_lazy as _

from .stakeholder_group import StakeholderGroup
# from .direct_indicator import DirectIndicator


class SurveyManager(models.Manager):
    def create(self, name, description, anonymous, method, rate=0):
        stakeholdergroup, _ = StakeholderGroup.objects.get_or_create(name="Employee")
        survey = Survey(name=name, description=description, rate=rate, anonymous=anonymous, method=method)
        survey.save()
        print('<<>>', survey.id)
        survey.stakeholder_groups.add(stakeholdergroup)
        print(survey.stakeholder_groups.all())
        # directindicators = DirectIndicator.objects.filter(topic__method=method.id)
        # print('---', directindicators)
        # for di in directindicators.iterator():
        #     print(di)
        #     survey.questions.add(di)
        return survey

class Survey(models.Model):
    objects = SurveyManager()
    name=models.CharField(max_length=255, unique=False, blank=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
    rate = models.IntegerField(default=0)
    anonymous = models.BooleanField(null=False)
    questions = models.ManyToManyField('DirectIndicator', blank=False)
    method =  models.ForeignKey('Method', related_name="surveys", on_delete=models.CASCADE)
    stakeholder_groups = models.ManyToManyField('StakeholderGroup')

    class Meta:
        verbose_name = _('survey')
        verbose_name_plural = _('surveys')

    def __str__(self):
        return self.name

        