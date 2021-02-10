from django.db import models


class Method(models.Model):
    ispublic = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    organisations = models.ManyToManyField('Organisation', related_name="methods", default=None)

    def __repr__(self):
         return (
             f"<Method id='{self.id}' name='{self.name}' "
             f"description='{self.description}' is_public='{self.ispublic}' "
             f"organization='{self.organisations}'>"
         )

    def __str__(self):
        return self.name