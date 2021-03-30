from django.db import models
from django.utils.translation import gettext_lazy as _


class QuestionResponse(models.Model):
    survey_response = models.ForeignKey('SurveyResponse', related_name='question_responses', on_delete=models.CASCADE)
    direct_indicator_id = models.IntegerField()
    # values
    

    class Meta:
        verbose_name = _('question_response')
        verbose_name_plural = _('question_responses')

    def __str__(self):
        return f"{self.survey_response.id}, {self.direct_indicator_id}, values: {self.values.all()}"