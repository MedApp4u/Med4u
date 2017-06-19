# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	username=forms.CharField(max_length=30,required=True, widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-username'}))
	first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-first_name'}))
	last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-last_name'}))
	email = forms.EmailField(max_length=254, help_text='Enter a valid email address only.',  widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-email'}))
	gender = forms.CharField(max_length=1, help_text='Enter M for Male and F for Female', label='Gender',required=True, widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-gender'}))
	dob=forms.DateField(required=True, label='Date of Birth', widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-dob'}))
	address=forms.CharField(required=False, label='Address', widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-address'}))
	mobile_no=forms.IntegerField(required=False, max_value=9999999999, label='Mobile No.', widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-mobile_no'}))
	blood_group=forms.CharField(required=False, label='Blood Group', widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': 'vp-form-field-blood_group'}))

	class Meta:
		model=Profile
		fields=('username','first_name','last_name','gender','email','dob','address','mobile_no','blood_group',)

