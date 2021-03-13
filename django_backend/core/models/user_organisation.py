from django.db import models

USERPERMISSIONS = (
    ('RU', 'RegularUser'),
    ('OA', 'OrganisationAdmin'),
    ('NA', 'NetworkAdmin'),
)

class UserOrganisation(models.Model):
    participant = models.ForeignKey('CustomUser', related_name='participants', on_delete=models.CASCADE)            #post instance.customuser_set.all()
    organisation = models.ForeignKey('Organisation', related_name='organisaions', on_delete=models.CASCADE)        # user instance.post_set.all()
    role = models.CharField(max_length=255, choices = USERPERMISSIONS, default='RU') # Could give permissions to a user based on their role

    class Meta:
        unique_together = [['participant', 'organisation']]
    
    def __str__(self):
        return f'{self.participant} - {self.organisation}'