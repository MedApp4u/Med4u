# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from ProfileApp.models import Profile
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from .choices import *


# Create your models here.
class Doctor(models.Model):

    doctor_name = models.CharField(max_length=100)
    doctor_phone_number = PhoneNumberField(blank=True)
    doctor_description = models.TextField()
    doctor_address = models.TextField(max_length=1000)
    doctor_speciality = models.CharField(max_length=60, choices=SPECIALITY_CHOICE, default="FAMILY MEDICINE PHYSICIAN")
    doctor_timings = models.CharField(max_length=30, default="06 AM to 06 PM")
    doctor_pic= models.ImageField(upload_to="doctors", null=True) #Insert upload_to
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.doctor_name

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration


class Doctor_Note(models.Model):
    doctor_note = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) 


class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    dosage_amt = models.CharField(max_length=30)
    method = models.CharField(max_length=1, choices=MEDICINE_CHOICES)
    frequency = models.IntegerField(help_text='No of times a day')
    # Frontend please write number per day on the side of the frequency field
    medicine_date = models.DateField(help_text='Start date of the prescription')
    doctor = models.ManyToManyField(Doctor)
    usage_instructions = models.TextField()
    overdose_instructions = models.TextField()
    possible_sideeffects = models.TextField()
    brand_names = models.TextField()
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)


    def __str__(self):
        return self.medicine_name

class Medicine_Note(models.Model):
    medicine_note = models.TextField()
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Bodypart(models.Model):
    bodypart = models.CharField(max_length=15, choices=BODYPART, default="head")

    def __str__(self):
        return self.bodypart


class Symptom(models.Model):
    symptom_name = models.CharField(max_length=60)
    symptom_description = models.TextField()
    tests = models.TextField()
    bodypart = models.ManyToManyField(Bodypart)
    
    def __str__(self):
        return self.symptom_name

class Sypmtom_Videos(models.Model): #Multi valued attribute
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    symptom_video = models.URLField()


class Procedure(models.Model):
    procedure_name = models.CharField(max_length=60)
    procedure_description = models.CharField(max_length=600)
    possible_complication = models.CharField(max_length=600)
    bodypart = models.ManyToManyField(Bodypart)
    symptom = models.ManyToManyField(Symptom)
    medicine = models.ManyToManyField(Medicine)
    doctor = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.procedure_name

class Procedure_Images(models.Model): #Multi valued attribute
    proc = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    procedure_image=models.ImageField(upload_to="procedures", null=True)

class Procedure_Videos(models.Model): #Multi valued attribute
    proc = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    procedure_video = models.URLField()

class Procedure_Helpline(models.Model): #Multi valued attribute
    proc = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    procedure_phone_number = PhoneNumberField(blank=True)

class Procedure_Note(models.Model):
    procedure_note = models.TextField()
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) 


class Disease(models.Model):
    disease_name=models.CharField(max_length=300)
    disease_date=models.DateField(help_text='Date the disease was acquired')
    symptom = models.ManyToManyField(Symptom)
    medicine = models.ManyToManyField(Medicine)
    procedure = models.ManyToManyField(Procedure)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.disease_name

class Disease_Note(models.Model):
    disease_note = models.TextField()
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Measurement(models.Model):
    blood_pressure = models.CharField(max_length=30)
    blood_sugar = models.CharField(max_length=30)
    cholesterol = models.CharField(max_length=30)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    date = models.DateField(default=datetime.date.today)
    notes = models.TextField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __iter__(self): 
        return [ self.blood_pressure, self.blood_sugar, self.cholesterol, self.height, self.weight, self.date, self.notes, self.user ]


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # mobile = user.(pk=pk).mobile
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    """time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
FRONTEND look at this for exit change
    [[[https://stackoverflow.com/questions/34841008/django-timefield-format]]]
"""
    reason = models.TextField()
    notes = models.TextField()
    

class Insurance(models.Model):
    insurance_plan = models.CharField(max_length=500)
    expiry_date = models.DateField()
    start_date = models.DateField()
    premium = models.IntegerField()
    notes = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.insurance_plan


class Document(models.Model):
    doc = models.FileField(upload_to="documents", null=True)
    notes = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
