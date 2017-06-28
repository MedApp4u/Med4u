# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .models import *
from django import forms


class DocumentForm(forms.ModelForm):
    doc = forms.ImageField(required=False, label='Upload Document')
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
