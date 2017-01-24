from __future__ import unicode_literals
from django import forms
from django.db import models


class Qa(models.Model):
    first = models.CharField(max_length=200) 
    last = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, blank=True, null= True, unique= True, default="")
    password = models.CharField(max_length=100, default="")
    age = models.IntegerField()
