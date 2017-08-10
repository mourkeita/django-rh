from __future__ import unicode_literals
from django import forms
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Qa(models.Model):
    first = models.CharField(max_length=200) 
    last = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True, default="")
    password = models.CharField(max_length=100, default="")
    age = models.IntegerField(max_length=3)

    # def __init__(self, first, last, email, password, age):
    # 	self.first = first
    # 	self.last = last
    # 	self.email =email
    # 	self.password = password
    # 	self.age = age

    def save(self, *args, **kwargs):
        print "Save object"
        super(Qa, self).save(*args, **kwargs)
