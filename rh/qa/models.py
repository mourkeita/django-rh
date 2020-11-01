from __future__ import unicode_literals
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Employee(models.Model):
    first = models.CharField(max_length=200) 
    last = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True, default="")
    password = models.CharField(max_length=100, default="")
    age = models.IntegerField()
    avatar = models.FileField()
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return str(self.first) + " " + str(self.last)

    def save(self, *args, **kwargs):
        #Encrypt password self.password = make_password(self.password)
        self.password = self.password
        #print "Save object"
        super(Employee, self).save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    telephone = models.CharField(max_length=20)
    siren = models.CharField(max_length=100)
    siret = models.CharField(max_length=100)
    activity = models.CharField(max_length=200)
    size = models.IntegerField()
    juridical_status = models.CharField(max_length=200, default="")
    social_capital = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(Company, self).save(*args, **kwargs)

class CompanyInformations(models.Model):
    company = models.ForeignKey(Company)
    category = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.company.name + " informations"

    def save(self, *args, **kwargs):
        super(CompanyInformations, self).save(*args, **kwargs)


class Employment(models.Model):
    employee = models.ForeignKey(Employee)
    company = models.ForeignKey(Company)
    employment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.first + " / " + self.company.name

    def save(self, *args, **kwargs):
        super(Employment, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('employee', 'company')


class Relationship(models.Model):
    sender = models.ForeignKey(Employee)
    #receiver = models.ForeignKey(Employees)
    request_date = models.DateTimeField(auto_now_add=True)
    response_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.sender.first

    def save(self, *args, **kwargs):
        super(Relationship, self).save(*args, **kwargs)

# class JobOffer(models.Model):
#     title = models.CharField(max_length=200)
#     location = models.CharField(max_length=100)
#     company = models.ForeignKey(Company)
#     jobOfferText = models.TextField(max_length=2000)
#     creation_date = models.DateTimeField(auto_now_add=True)
#     private = models.BooleanField()
#
#     def save(self, *args, **kwargs):
#         super(JobOffer, self).save(*args, **kwargs)
