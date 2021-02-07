from django.db import models

class UserOrganisation(models.Model):
    participant = models.ForeignKey('CustomUser', related_name='participants', on_delete=models.CASCADE) #post instance.customuser_set.all()
    organisation = models.ForeignKey('Post', related_name='organisations', on_delete=models.CASCADE) # user instance.post_set.all()

    class Meta:
        unique_together = [['participant', 'organisation']]