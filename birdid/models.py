from django.conf import settings
from django.db import models


# Create your models here.

class Waterbird(models.Model):
    name = models.CharField(max_length = 100)
    back_color = models.CharField(max_length = 100)
    breast_color = models.CharField(max_length = 100)
    bill_size = models.CharField(max_length = 100)
    leg_length = models.CharField(max_length = 100)
    call_complexity = models.CharField(max_length = 100)
    water_type = models.CharField(max_length = 100)
    description = models.TextField()
    image_bird = models.ImageField(default='fallback.png', blank=True)

def __str__(self):
    return self.name

class Raptor(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    image_bird = models.ImageField(upload_to='images/', default='coopers_hawk.jpg', blank=True, null=True)

def __str__(self):
    return self.name


class Songbird(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    image_bird = models.ImageField(upload_to='images/', default='fallback.png', blank=True, null=True)

def __str__(self):
    return self.name

