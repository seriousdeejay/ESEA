'''
from django.db import models

class Report(models.Model):
    method_organisations = models.ForeignKey('MethodOrganisation', related_name="report", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    certification_grades = models.ManyToManyField('CertificationGrade', related_name="report", blank=True)

    def __str__(self):
        return self.name
'''