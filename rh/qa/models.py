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
    age = models.IntegerField()
    avatar = models.FileField()

    def save(self, *args, **kwargs):
        #Encrypt password self.password = make_password(self.password)
        self.password = self.password
        print "Save object"
        super(Qa, self).save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    telephone = models.CharField(max_length=20)
    siren = models.CharField(max_length=100)
    siret = models.CharField(max_length=100)
    activity = models.CharField(max_length=200)
    size = models.IntegerField()
    
    def save(self, *args, **kwargs):
        super(Company, self).save(*args, **kwargs)


class Employment(models.Model):
    company = models.ForeignKey(Company)
    employee = models.ForeignKey(Qa)
    employment_date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super(Employment, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('company', 'employee')