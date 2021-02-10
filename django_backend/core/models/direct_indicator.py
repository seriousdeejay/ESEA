from django.db import models
from django.utils.translation import gettext_lazy as  _


class DirectIndicator(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', related_name='direct_indicators', on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('direct_indicators')
        verbose_name_plural = _('direct_indicators')

    def __str__(self):
        return self.question.name

# Not totally filled in