from __future__ import unicode_literals

from django.db import models


class Qa(models.Model):
    name = models.CharField(max_length=200) 
    first_name = models.CharField(max_length=200)
    age = models.IntegerField()
# Create your models here.
