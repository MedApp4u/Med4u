# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import *
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from ProfileApp.models import Profile
from MyHealthApp.models import *
import os

# Create your views here.

class LoginFormView(View):
    form_class = LoginForm
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})

    def post(self, request):
        form = self.form_class(None)
        # cleaned (normalized) data

        context = ""
        username = request.POST['username']
        password = request.POST['password']

        # returns User objects if credentials are correct
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                context = "User is banned"
        else:
            context = "Incorrect username or password"

        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})


class UserFormView(View):
    form_class = UserForm
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})

    def post(self, request):
        form = self.form_class(request.POST)
        context = ""

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username1 = form.cleaned_data['username1']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                context = "Passwords do not match."
                return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})
            user.set_password(password1)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username1, password=password1)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    context = "Existing user is banned."

        else:
            context = "Please select a unique username."

        return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})


def redirect_to_dashboard(request):
    return HttpResponseRedirect('/dashboard/')


class Tnc(generic.TemplateView):
    template_name = 'GeneralApp/tnc.html'


class AboutUs(generic.TemplateView):
    template_name = 'GeneralApp/about.html'


class SymptomsView(generic.TemplateView):
    template_name = 'GeneralApp/symptoms.html'
    

def SymptomHead(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='head')
        return  render(request,'GeneralApp/symptomhead.html',{'x': a})

def SymptomAbdomen(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='abdomen')
        return  render(request,'GeneralApp/symptomabdomen.html',{'x': a})

def SymptomArms(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='arms')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})


def SymptomChest(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='chest')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomFeet(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='feet')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})


def SymptomHands(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='hands')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomHips(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='hips')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomLegs(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='legs')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomNeck(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='neck')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomPelvis(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='pelvis')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})



def SymptomShoulder(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='shoulder')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})


def procedures(request):
    procedures_list = Procedure.objects.all()

    if request.method == 'GET':
        return render(request, 'GeneralApp/procedures.html', {'procedures': procedures_list, 'current_user': request.user})


def procedure_details(request, proc_id):
    procedures_list = Procedure.objects.all()
    current_procedure = Procedure.objects.get(id=proc_id)
    bodyparts = Bodypart.objects.filter(procedure__id=proc_id)
    symptoms = Symptom.objects.filter(procedure__id=proc_id)
    medicines = Medicine.objects.filter(procedure__id=proc_id)
    doctors = Doctor.objects.filter(procedure__id=proc_id)
    p = Procedure.objects.get(pk=proc_id)
    images = p.procedure_images_set.all()
    videos = p.procedure_videos_set.all()
    helplines = p.procedure_helpline_set.all()

    if request.method == 'GET':
        return render(request, 'GeneralApp/procedures-test.html', {'procedures': procedures_list, 'current_user': request.user, 
            'current_procedure': current_procedure, 'bodyparts': bodyparts, 'symptoms': symptoms, 'medicines': medicines, 'doctors': doctors, 
            'images': images, 'videos': videos, 'helplines': helplines})


def doctors(request):
    doctors_list = Doctor.objects.all()

    if request.method == 'GET':
        return render(request, 'GeneralApp/find-doctors.html', {'doctors': doctors_list, 'current_user': request.user})

def doctor_details(request, doc_id):
    doctors_list = Doctor.objects.all()
    current_doctor = Doctor.objects.get(id=doc_id)

    if request.method == 'GET':
        return render(request, 'GeneralApp/doctors-list.html', {'doctors': doctors_list, 'current_user': request.user, 'current_doctor': current_doctor})


def medicines(request):
    medicines_list = Medicine.objects.all()

    if request.method == 'GET':
        return render(request, 'GeneralApp/medicines.html', {'medicines': medicines_list, 'current_user': request.user})

def medicine_details(request, med_id):
    medicines_list = Medicine.objects.all()
    current_medicine = Medicine.objects.get(id=med_id)
    # add_medicine_form = AddGeneralMedicineForm()
    # add_medicine_form.fields['medc_id'] = med_id
    # print add_medicine_form.fields['medc_id'] 

    if request.method == 'GET':
        return render(request, 'GeneralApp/medicine_details.html', {'medicines': medicines_list, 'current_user': request.user, 'current_medicine': current_medicine})


def AddGeneralMedicine(request):
    current_user = request.user

    if request.method == 'POST':
        id = request.POST['med_id']
        current_user.medicine_set.add(Medicine.objects.get(pk=id))

    return HttpResponseRedirect('/my_medicines/' + str(id))

def AddGeneralDoctor(request):
    current_user = request.user

    if request.method == 'POST':
        id = request.POST['doc_id']
        current_user.doctor_set.add(Doctor.objects.get(pk=id))

    return HttpResponseRedirect('/my_doctors/' + str(id))

# def procedures(request):
#     context = ""
#     # profile=Profile.objects.get(username=request.user.username)

#     if request.method == 'GET':
#         form = ProcedureForm(None)
#         return render(request, 'GeneralApp/procedures_form.html', {'form': form, 'context': context, 'current_user': request.user})

#     if request.method == 'POST':
#         bp = request.POST['bodypart']
#         file_write(bp)
#         form = ProcedureForm(request.POST)
#         return render(request, 'GeneralApp/procedures_form.html', {'form': form, 'context': context, 'current_user': request.user})

# def file_write(bp):
#     queryset = Symptom.objects.filter(bodypart__bodypart=bp)
#     f = open(os.path.join('GeneralApp/', 'choices.py'), 'w')
#     if queryset is not None:
#         f.write('SYMPTOMS = (')
#         for item in queryset:
#             f.write("('" + str(item) + "', '" + str(item) + "'), ")
#         f.write(')')
        
#     else:
#         f.write('SYMPTOMS = (("-","-""),)')
#     f.close()

    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, instance=profile)
    #     context = ""
    #     form.save()
    #     return HttpResponseRedirect('/view_profile/')
