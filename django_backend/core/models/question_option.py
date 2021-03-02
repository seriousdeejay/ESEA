from django.db import models
from ..apps import AppConfig


class QuestionOption(models.Model):
    text = models.CharField(max_length=140, blank=False)
    value = models.IntegerField(blank=False)
    question = models.ForeignKey('Question', related_name="question_options", on_delete=models.CASCADE)

    class Meta:
        db_table = 'f{AppConfig.name}_question_option'
    
    def equal(self, data):
        return self.text == data['text'] and self.value == data['value']
    
    def __str__(self):
        return f"{self.text}"

    def __repr__(self):
        return (f"<QuestionOption id='{self.id}', text='{self.text} '"
                f"value='{self.value}' question='{self.question}'")