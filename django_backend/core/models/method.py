from django.db import models
from .customuser import CustomUser

class Method(models.Model):
    ispublic = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    # creator = models.ForeignKey('CustomUser', null=True, blank=True, default= None, editable=False, related_name='method_creator', on_delete=models.SET_DEFAULT) # change to foreignkey
    organisations = models.ManyToManyField('Organisation', related_name="methods", blank=True)

    def __repr__(self):
         return (
             f"<Method id='{self.id}' name='{self.name}' "
             f"description='{self.description}' is_public='{self.ispublic}' "
             f"organization='{self.organisations}'>"
         )

    def __str__(self):
        return self.name