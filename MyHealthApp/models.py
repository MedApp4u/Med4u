# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from ProfileApp.models import Profile
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from .choices import *
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
def doctor_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/documents/user_<id>/<filename>
    return 'doctor/doctor_{0}/{1}'.format(instance.id, filename)


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_phone_number = PhoneNumberField(blank=True)
    doctor_description = models.TextField(blank=True)
    doctor_address = models.TextField(max_length=1000, blank=True)
    doctor_speciality = models.CharField(max_length=60, choices=SPECIALITY_CHOICE, default="FAMILY MEDICINE PHYSICIAN",
                                         blank=True)
    doctor_timings = models.CharField(max_length=30, default="06 AM to 06 PM")
    doctor_pic = models.ImageField(upload_to=doctor_directory_path, null=True, blank=True)  # Insert upload_to
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.doctor_name

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration


class Doctor_Note(models.Model):
    doctor_note = models.TextField(blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    dosage_amt = models.CharField(max_length=30, blank=True)
    method = models.CharField(max_length=1, choices=MEDICINE_CHOICES, blank=True)
    frequency = models.IntegerField(help_text='No of times a day', blank=True)
    # Frontend please write number per day on the side of the frequency field
    medicine_date = models.DateField(help_text='Start date of the prescription', blank=True)
    doctor = models.ManyToManyField(Doctor, related_name='prescription', blank=True)
    usage_instructions = models.TextField(blank=True)
    overdose_instructions = models.TextField(blank=True)
    possible_sideeffects = models.TextField(blank=True)
    brand_names = models.TextField(blank=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.medicine_name


class Medicine_Note(models.Model):
    medicine_note = models.TextField(blank=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Bodypart(models.Model):
    bodypart = models.CharField(max_length=15, choices=BODYPART, default="head")

    def __str__(self):
        return self.bodypart


class Symptom(models.Model):
    symptom_name = models.CharField(max_length=60)
    symptom_description = models.TextField(blank=True)
    tests = models.TextField(blank=True)
    bodypart = models.ManyToManyField(Bodypart, related_name='BPsymptom')
    
    def __str__(self):
        return self.symptom_name


class Symptom_Videos(models.Model):  # Multi valued attribute
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    symptom_video = models.URLField(blank=True)


def procedure_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/documents/user_<id>/<filename>
    return 'procedures/procedure_{0}/{1}'.format(instance.proc, filename)


class Procedure(models.Model):
    procedure_name = models.CharField(max_length=60)
    procedure_description = models.CharField(max_length=600, blank=True)
    possible_complication = models.CharField(max_length=600, blank=True)
    bodypart = models.ManyToManyField(Bodypart, blank=True)
    symptom = models.ManyToManyField(Symptom, blank=True)
    medicine = models.ManyToManyField(Medicine, blank=True)
    doctor = models.ManyToManyField(Doctor, blank=True)

    def __str__(self):
        return self.procedure_name


class Procedure_Images(models.Model):  # Multi valued attribute
    proc = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    procedure_image = models.ImageField(upload_to=procedure_directory_path, null=True, blank=True)


class Procedure_Videos(models.Model):  # Multi valued attribute
    proc = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    procedure_video = models.URLField(blank=True)


class Procedure_Helpline(models.Model):  # Multi valued attribute
    proc = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    procedure_phone_number = PhoneNumberField(blank=True)



class Disease(models.Model):
    disease_name = models.CharField(max_length=300)
    disease_description = models.TextField(blank=True)
    disease_date = models.DateField(help_text='Date the disease was acquired', blank=True)
    symptom = models.ManyToManyField(Symptom, related_name='dis_symptom', blank=True)
    medicine = models.ManyToManyField(Medicine, blank=True)
    procedure = models.ManyToManyField(Procedure, blank=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.disease_name


class Disease_Note(models.Model):
    disease_note = models.TextField(blank=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Measurement(models.Model):
    blood_pressure = models.CharField(max_length=30, blank=True)
    blood_sugar = models.CharField(max_length=30, blank=True)
    cholesterol = models.CharField(max_length=30, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    notes = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __iter__(self):
        return [self.blood_pressure, self.blood_sugar, self.cholesterol, self.height, self.weight, self.date,
                self.notes, self.user]


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # mobile = user.(pk=pk).mobile
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(blank=True)
    notes = models.TextField(blank=True)


class Insurance(models.Model):
    insurance_plan = models.CharField(max_length=500)
    expiry_date = models.DateField(blank=True)
    start_date = models.DateField(blank=True)
    premium = models.IntegerField(blank=True)
    notes = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.insurance_plan


def document_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/documents/user_<id>/<filename>
    return 'documents/user_{0}/{1}'.format(instance.user.id, filename)


def doc_half_name(x):
    name = x
    count = 0
    cnt=0
    j = 13
    string = []
    for i in name:
        if i == '/':
            count = count + 1;
        if count >= 2 and j >= 0:
            j = j - 1
            string.append(i)
    if len(string) >= 14:

        string = string + ['.','.','.']

        for i in name:
            if i == '.':
                cnt = cnt+1
            if cnt >= 1:
                string.append(i)
       
    return ''.join(string)

def doc_full_name(x):
    name = x
    count = 0
    string = []
    for i in name:
        if i == '/':
            count = count + 1;
        if count >= 2 :
            string.append(i)
    return ''.join(string)

class Document(models.Model):
    doc = models.FileField(upload_to=document_directory_path, null=True, blank=True)
    notes = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    

    def doc_half_name(self):
        return doc_half_name(self.doc.name)

    def doc_name(self):
        return doc_full_name(self.doc.name)

    




