# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ProfileApp.models import Profile
from MyHealthApp.models import *

# Appointment, Procedure, Insurance, Symptom, 

# Register your models here.
# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ('username', 'email')


admin.site.register(Profile)

admin.site.register(Appointment)
admin.site.register(Procedure)
admin.site.register(Insurance)
admin.site.register(Symptom)
admin.site.register(Bodypart)
admin.site.register(Medicine)
admin.site.register(Doctor)
admin.site.register(Measurement)