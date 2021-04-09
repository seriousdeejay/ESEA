from django.db import models
from django.utils.translation import gettext_lazy as  _

from .question import Question


class directIndicatorManager(models.Manager):
    def create(self, isMandatory, key, topic, name, answertype, survey,
        description=None, instruction=None, max_number=None, min_number=None, options=None):
        question = Question.objects.create(name=name, isMandatory=isMandatory, answertype=answertype, topic=topic, description=description, instruction=instruction, options=options)
        direct_indicator = DirectIndicator(key=key, max_number=max_number, min_number=min_number, question=question, topic=topic)
        direct_indicator.save()
        survey.questions.add(direct_indicator)

        return direct_indicator


class DirectIndicator(models.Model):
    objects = directIndicatorManager()
    key = models.CharField(max_length=45, blank=False)
    min_number = models.IntegerField(null=True)
    max_number = models.IntegerField(null=True)
    question = models.ForeignKey("Question", related_name="direct_indicators", on_delete=models.CASCADE)
    topic = models.ForeignKey("Topic", related_name="direct_indicators", on_delete=models.CASCADE)
    responses = []
    value = None
    calculation_keys = None
    calculation = None

    class Meta:
        verbose_name = _("direct_indicator")
        verbose_name_plural = _("direct_indicators")

    @property
    def name(self):
        return self.question.name

    def __str__(self):
        return self.question.name

    def update(self, isMandatory, key, topic, name, answertype, options=None, description=None, instruction=None, min_number=None, max_number=None):
        self.key = key
        self.min_number = min_number
        self.max_number = max_number
        self.topic = topic
        self.question = self.question.update(name=name, answertype=answertype, options=options, description=description, instruction=instruction)
        self.save()
        return self

    def filter_responses(self, responses):
        self.responses = [
            response.values
            for response in responses
            if response.direct_indicator_id == self.id
        ]
        self.value = self.get_average(self.responses)

    def get_average(self, responses=[]):
        response_values = responses
        if not len(responses):
            return "0"

        if (
            self.question.answertype == self.question.RADIO
            or self.question.answertype == self.question.CHECKBOX
        ):
            response_values = self.checkbox_values(responses)
            return response_values


        return self.average_calculation(response_values)

    def average_calculation(self, responses):
        numbers = [int(r) for r in responses]
        return sum(numbers) / len(numbers)

    def checkbox_values(self, responses):
        valuesdict = {}
        for option in self.question.options.all():
            valuesdict[option.text] = 0
        #print(valuesdict['Fixed Salary'])
        for response in responses:
            # options = response.split(",") # Splits it on commas, should be changed!!!
            for option in response.all():
                if option:
                    question_option = self.question.options.filter(text=option).first()
                    if question_option:
                        valuesdict[question_option.text] += 1
        return valuesdict

'''
- Should response_values not be returned to self.value (or self.values)?  [FIXED]
'''