from django.db import models

# STATUS = (
#     ('Complete', 'Complete'),
#     ('Incomplete', 'Incomplete'),
#     ('Ongoing', 'Ongoing'),
# # )

class EseaAccount(models.Model):
    organisation = models.ForeignKey("Organisation", on_delete=models.CASCADE)
    method = models.ForeignKey("Method", on_delete=models.CASCADE)
    campaign = models.ForeignKey('Campaign', related_name="organisation_accounts", on_delete=models.CASCADE)
    # report = models.OneToOneField('Report')
    # response_rate = 

    def __str__(self):
        return f'organisation:{self.organisation} - campaign:{self.campaign}'
    

