'''
from django.db import models
from django.utils.timezone import now

class NetworkMethod(models.Model):
    network = models.ForeignKey("Network", related_name="network_methods", on_delete=models.CASCADE)
    method = models.ForeignKey("method", related_name="method_networks", on_delete=models.CASCADE) # If a method gets removed the network_method gets removed too, is this a good choice?
    created_by = models.ForeignKey('CustomUser', editable=False, on_delete=models.SET_NULL, null=True) # related_name='method_creator'
    created_on = models.DateTimeField(default=now, editable=False)
    required = models.BooleanField(default=True)
'''