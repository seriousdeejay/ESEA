from django.db import models

USERPERMISSIONS = (
    ('RU', 'RegularUser'),
    ('OA', 'OrganisationAdmin'),
    ('NA', 'NetworkAdmin'),
)

class UserOrganisation(models.Model):
    user = models.ForeignKey("CustomUser", related_name='user_organisations', on_delete=models.CASCADE)            #post instance.customuser_set.all()
    organisation = models.ForeignKey("Organisation", related_name='organisation_members', on_delete=models.CASCADE)        # user instance.post_set.all()
    role = models.CharField(max_length=255, choices = USERPERMISSIONS, default='RU') # Could give permissions to a user based on their role
    stakeholdergroups = models.ManyToManyField('StakeholderGroup', blank=True)

    class Meta:
        unique_together = [['user', 'organisation']]
    
    def __str__(self):
        return f'{self.user} - {self.organisation}'

        # o.organisation_members.filter(stakeholdergroups=...)
        # o.organisation.members.all()  --> All UserOrganisation instances with organisation=o
        # o.members.all()   All members
        # u.user_organisations.all() --> All UserOrganisation instances with user=u
        # u.accessible_organisations.all()