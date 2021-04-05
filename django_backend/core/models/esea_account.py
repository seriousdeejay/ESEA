from django.db import models

# STATUS = (
#     ('Complete', 'Complete'),
#     ('Incomplete', 'Incomplete'),
#     ('Ongoing', 'Ongoing'),
# # )

class EseaAccount(models.Model):
    sufficient_responses = models.BooleanField(default=False)
    organisation = models.ForeignKey("Organisation", on_delete=models.CASCADE)
    method = models.ForeignKey("Method", on_delete=models.CASCADE)
    campaign = models.ForeignKey('Campaign', related_name="organisation_accounts", on_delete=models.CASCADE)
    # 
    # responses (Many to one Relationship with survey_response)
    #response_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f'organisation:{self.organisation} - campaign:{self.campaign}'
    

    @property
    def response_rate(self):
        response_rate_dict = {}
        overall_finished_responses = 0
        for survey in self.method.surveys.all():
            finished_responses = [response for response in self.responses.all() if (response.finished == True & response.survey == survey)]
            overall_finished_responses += len(finished_responses)
            sum = (len(finished_responses)/(len(self.responses.all()) or 1) * 100) 
            sum = round(sum,2)
            response_rate_dict[survey.name] = {'rate': sum, 'required': survey.rate}
        self.all_response_rate(overall_finished_responses)
        return response_rate_dict

    def sufficient_response_rate(self):
        Bool = True
        for survey in self.response_rate:
            innerdict = self.response_rate[survey]
            if (innerdict['rate'] >= innerdict['required']):
                print(f'The response rate of {survey} is high enough!')
            else:
                print(f'The response rate of {survey} is not high enough!')
                Bool = False

        self.sufficient_responses = Bool
    
    def all_response_rate(self, finished_responses):
        self.all_response_rate = (finished_responses/(len(self.responses.all()) or 1)) * 100
            
''' 
- Should change __str__ return
'''