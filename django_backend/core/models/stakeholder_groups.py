from django.db import models
from django.utils.translation import gettext_lazy as _

class StakeholderGroups(models.Model):
    name=models.CharField(max_length=100, unique=true)
    description=models.CharField(max_length=1000)
    
    
## Redundant Model?