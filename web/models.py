from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(
        max_length=100, default='', blank=False, null=False)
    power = models.IntegerField(default=0, blank=False, null=False)
    icon = models.CharField(max_length=1000, default='', blank=True, null=True)
    speciality = models.CharField(
        max_length=1000, default='', blank=True, null=True)
    is_god = models.BooleanField(default=False, blank=True)
