# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import *



class DoctorSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile-detail')
    class Meta:
        model = Doctor
        fields=('doctor_name','doctor_phone_number','doctor_description','doctor_address','doctor_speciality','doctor_timings','doctor_pic','user')

class Doctor_NoteSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile-detail')
    class Meta:
        model = Doctor_Note
        fields=('doctor_note','doctor','user')



class MedicineSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    doctor =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile-detail')
    #doctor = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Doctor-detail')
    class Meta:
        model = Medicine
        fields=('medicine_name','dosage_amt','method','frequency','medicine_date','doctor','usage_instructions','overdose_instructions','possible_sideeffects','brand_names','user')

class Medicine_NoteSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile-detail')
    class Meta:
        model = Medicine_Note
        fields=('medicine_note','medicine','user')
       
 
class BodypartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodypart
        fields=('bodypart',)

        
class SymptomSerializer(serializers.ModelSerializer):
    #bodypart = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Bodypart-detail')
    bodypart = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Symptom
        fields=('symptom_name','bodypart','symptom_description','tests')



class Symptom_VideosSerializer(serializers.ModelSerializer):
    bodypart =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #bodypart = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Bodypart-detail')
    class Meta:
        model = Sypmtom_Videos
        fields=('symptom','symptom_video')

class InsuranceSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Profile-detail)
    class Meta:
        model = Insurance
        fields=('insurance_plan','expiry_date','start_date','user')

        
class ProcedureSerializer(serializers.ModelSerializer):
    medicine=  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    doctor =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    symptom =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    bodypart =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #bodypart= serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Bodypart-detail)
    #symptom = serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Symptom-detail)
    #medicine = serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Medicine-detail)
    #doctor = serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Doctor-detail)
    class Meta:
        model = Procedure
        fields=('procedure_name','procedure_description','possible_complication','doctor','bodypart','symptom','medicine')

class Procedure_ImagesSerializer(serializers.ModelSerializer):
    proc =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #proc = serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Procedure-detail)
    class Meta:
        model = Procedure_Images
        fields=('procedure_image','proc')

class Procedure_VideosSerializer(serializers.ModelSerializer):
    proc =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #proc = serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Procedure-detail)
    class Meta:
        model = Procedure_Videos
        fields=('procedure_video','proc')


class Procedure_HelplineSerializer(serializers.ModelSerializer):
    proc =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #proc = serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Procedure-detail)
    class Meta:
        model = Procedure_Helpline
        fields=('procedure_phone_number','proc')


class Procedure_NoteSerializer(serializers.ModelSerializer):
    proc =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #proc = serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Procedure-detail)
    #user = serializers.HyperlinkedRelatedField(many=True, read-only=True,view_name=Profile-detail)
    class Meta:
        model = Procedure_Note
        fields=('procedure_note','procedure','user')
        
class DiseaseSerializer(serializers.ModelSerializer):
    symptom=  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    medicine=  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    procedure =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile_show')
    #procedure = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Procedure-detail')
    #medicine = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Medicine-detail')
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Symptom_detail')
    class Meta:
        model = Disease
        fields=('disease_name','disease_date','symptom','medicine','procedure','user')

        
class Disease_NoteSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    disease =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile_show')
    #disease= serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Disease_show')
    
    class Meta:
        model = Disease_Note
        fields=('disease_note','disease','user')

    


class MeasurementSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile-detail')
    class Meta:
        model = Measurement
        fields=('blood_pressure','blood_sugar','cholesterol','height','weight','user','date','notes')

                
                
class AppointmentSerializer(serializers.ModelSerializer):
    doctor =  serializers.PrimaryKeyRelatedField(many =False,read_only=True)
    user =  serializers.PrimaryKeyRelatedField(many =False,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile_show')
    #doctor = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Doctor_show')
    class Meta:
        model = Appointment
        fields=('doctor','user','date','time','reason','notes')



class InsuranceSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile_show')
    
    class Meta:
        model = Insurance
        fields=('insurance_plan','expiry_date','start_date','premium','notes','user')

class DocumentSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(many =True,read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Profile_show')
    class Meta:
        model = Document
        fields=('doc','notes','user')

class Procedure_ImagesSerializer(serializers.ModelSerializer):
    proc = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    #proc = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Procedure_show')
    class Meta:
        model = Procedure_Images
        fields=('proc','procedure_image')

class Procedure_VideosSerializer(serializers.ModelSerializer):
    proc = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    #proc = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Procedure_show')
    class Meta:
        model = Procedure_Images
        fields=('proc','procedure_videos')

class Procedure_HelplineSerializer(serializers.ModelSerializer):
    proc = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    #proc= serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Procedure-detail')
    class Meta:
        model = Procedure_Helpline
        fields=('proc','procedure_phone_number')

class Procedure_NoteSerializer(serializers.ModelSerializer):
    proc = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    #proc= serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Procedure-detail')
    class Meta:
        model = Procedure_Note
        fields=('proc','procedure_note')