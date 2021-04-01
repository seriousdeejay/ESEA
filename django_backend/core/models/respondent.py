from django.db import models

class Respondent(models.Model):
    organisation = models.ForeignKey('Organisation', related_name="surveyrespondents", on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=75, blank=False)
    first_name = models.CharField(max_length=50)
    last_name_prefix = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        if self.last_name_prefix:
            return(f"{self.first_name} {self.last_name_prefix} {self.last_name}")
        return(f"{self.first_name} {self.last_name}")
