# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ProfileApp.models import Profile
from MyHealthApp.models import *

# Register your models here.
# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ('username', 'email')


admin.site.register(Profile)
#admin.site.register(Profile, ProfileAdmin)
admin.site.register(Appointment)
admin.site.register(Procedure)
admin.site.register(Insurance)
admin.site.register(Symptom)
admin.site.register(Bodypart)
admin.site.register(Medicine)
admin.site.register(Doctor)
admin.site.register(Doctor_Note)
admin.site.register(Medicine_Note)
admin.site.register(Sypmtom_Videos)
admin.site.register(Procedure_Images)
admin.site.register(Procedure_Videos)
admin.site.register(Procedure_Helpline)
admin.site.register(Procedure_Note)
admin.site.register(Disease)
admin.site.register(Disease_Note)
admin.site.register(Document)
admin.site.register(Measurement)
