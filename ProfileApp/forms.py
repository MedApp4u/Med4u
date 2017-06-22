# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Profile
from .choices import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ProfileForm(forms.ModelForm):
	username=forms.CharField(max_length=30,required=True, widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-username'}))
	first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-first_name'}))
	last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-last_name'}))
	email = forms.EmailField(max_length=254, help_text='Enter a valid email address only.',  widget=forms.EmailInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-email'}))
	gender = forms.ChoiceField(choices=SEX_CHOICES, help_text='Enter M for Male and F for Female', label='Sex',required=True, widget=forms.RadioSelect(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-gender'}))
	dob=forms.DateField(required=True, label='Date of Birth', widget=forms.DateInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-dob'}))
	address=forms.CharField(required=False, label='Address', widget=forms.Textarea(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-address'}))
	phone_number=PhoneNumberField(required=False, label='Mobile No.', widget=PhoneNumberPrefixWidget(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-mobile_no'}))
	blood_group=forms.ChoiceField(choices=BLOOD_GROUP_CHOICES,required=False, label='Blood Group',initial='Select', widget=forms.Select(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-blood_group'}))

	class Meta:
		model=Profile
		fields=('username','first_name','last_name','gender','email','dob','address','phone_number','blood_group',)