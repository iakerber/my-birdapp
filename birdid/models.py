from django.conf import settings
from django.db import models
#from django.utils import timezone

# Create your models here.

class Waterbird(models.Model):
    name = models.CharField(max_length = 100)
    back_color = models.CharField(max_length = 100)
    breast_color = models.CharField(max_length = 100)
    bill_size = models.CharField(max_length = 100)
    leg_length = models.CharField(max_length = 100)
    call_complexity = models.CharField(max_length = 100)
    water_type = models.CharField(max_length = 100)

def __str__(self):
    return self.name

