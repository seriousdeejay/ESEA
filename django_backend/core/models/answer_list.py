from django.db import models

class AnswerList(models.Model):
    pass
    # question_response = models.ForeignKey('QuestionResponse', related_name='values', on_delete=models.CASCADE)
    # value = models.TextField(max_length=1000)