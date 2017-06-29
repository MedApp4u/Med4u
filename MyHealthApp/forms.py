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
        fields = (
            'doctor_name', 'doctor_description', 'doctor_address', 'doctor_speciality', 'doctor_timings', 'doctor_pic')


class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none(), label='Doctor')
    date = forms.DateField()
    time = forms.TimeField()
    reason = forms.CharField(required=False, label='Reason', widget=forms.Textarea())
    notes = forms.CharField(required=False, label='Notes', widget=forms.Textarea())

    class Meta:
        model = Appointment
        fields = ('doctor', 'date', 'time', 'reason', 'notes')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = user.doctor_set.all()


class MedicineForm(forms.ModelForm):
    medicine_name = forms.CharField(required=True, label='Name')
    method = forms.ChoiceField(required=True, choices=MEDICINE_CHOICES)
    dosage_amt = forms.CharField(required=True, label='Amount')
    frequency = forms.IntegerField(help_text='No of times a day', required=True, label='Frequency')
    medicine_date = forms.DateField(help_text='Start date of the prescription', required=False, label='Start Date')
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none(), label='Doctor')
    usage_instructions = forms.CharField(required=True, label='Usage Instruction')
    overdose_instructions = forms.CharField(required=False, label='Overdose Instruction', widget=forms.Textarea())
    possible_sideeffects = forms.CharField(required=False, label='Possible Sideffects', widget=forms.Textarea())
    brand_names = forms.CharField(required=True, label='Brand Name', widget=forms.Textarea())

    class Meta:
        model = Medicine
        fields = (
            'medicine_name', 'method', 'dosage_amt', 'frequency', 'medicine_date', 'doctor', 'usage_instructions',
            'overdose_instructions', 'possible_sideeffects', 'brand_names')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MedicineForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = user.doctor_set.all()


class DiseaseForm(forms.ModelForm):
    symptom = forms.ModelMultipleChoiceField(required=True, label='Symptom', queryset=Symptom.objects.all())
    medicine = forms.ModelMultipleChoiceField(required=True, label='Medicine', queryset=Medicine.objects.none())
    procedure = forms.ModelMultipleChoiceField(required=True, label='Procedure', queryset=Procedure.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DiseaseForm, self).__init__(*args, **kwargs)
        self.fields['medicine'].queryset = user.medicine_set.all()

    class Meta:
        model = Disease
        exclude = ['user']
