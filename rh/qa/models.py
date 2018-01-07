from __future__ import unicode_literals
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Qa(models.Model):
    first = models.CharField(max_length=200) 
    last = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True, default="")
    password = models.CharField(max_length=100, default="")
    age = models.IntegerField(max_length=3)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        print "Save object"
        super(Qa, self).save(*args, **kwargs)



