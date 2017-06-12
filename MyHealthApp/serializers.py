# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import *



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields=('name','mobile','description','address','speciality','timings')


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields=('name','dossage_amt','method','frequency','date','notes','doctors')


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields=('blood_pressure','blood_sugar','cholesterol','height','weight','user')

 
class BodypartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodypart
        fields=('medicine')

        
class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields=('symptom_name','bodypart','medicine',)


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields=('insurance_plan','expiry_date','start_date','user')

        
class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields=('name','description','possible_complication','image','video','bodypart','symptom','medicine')
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields=('doctor','user','date','time',)







       



