# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .models import *
from django import forms
from .choices import *


class DocumentForm(forms.ModelForm):
    doc = forms.FileField(required=False, label='Upload Document')
    notes = forms.CharField(required=False, label='Notes', widget=forms.Textarea())

    class Meta:
        model = Document
        fields = ('doc', 'notes')


class InsuranceForm(forms.ModelForm):
    insurance_plan = forms.CharField(required=True, label='Insurance Plan')
    expiry_date = forms.DateField(required=True, label='Expiry Date')
    start_date = forms.DateField(required=True, label='Start Date')
    premium = forms.IntegerField(required=True, label='Premium Amount')
    notes = forms.CharField(required=False, label='Notes', widget=forms.Textarea())

    class Meta:
        model = Insurance
        fields = ('insurance_plan', 'expiry_date', 'start_date', 'premium', 'notes')


class MeasurementForm(forms.ModelForm):
    blood_pressure = forms.CharField(required=False, label='Blood Pressure')
    blood_sugar = forms.CharField(required=False, label='Blood Sugar')
    cholesterol = forms.CharField(required=False, label='Cholesterol')
    height = forms.FloatField(required=True, label='Height')
    weight = forms.FloatField(required=True, label='Weight')
    notes = forms.CharField(required=False, label='Notes', widget=forms.Textarea())


    class Meta:
        model = Measurement
        fields = ('blood_pressure', 'blood_sugar', 'cholesterol', 'height', 'weight', 'notes')


class DoctorForm(forms.ModelForm):
    doctor_name = forms.CharField(required=True, label='Name')
    doctor_description = forms.CharField(required=False, label='Description', widget=forms.Textarea())
    doctor_address = forms.CharField(required=True, label='Address', widget=forms.Textarea())
    doctor_speciality = forms.ChoiceField(required=True, choices=SPECIALITY_CHOICE, label='Speciality')
    doctor_timings = forms.CharField(required=True, label='Timing')
    doctor_pic = forms.ImageField(required=False, label='Upload Photo')


    class Meta:
        model = Doctor
        fields = ('doctor_name', 'doctor_description', 'doctor_address', 'doctor_speciality', 'doctor_timings', 'doctor_pic')

