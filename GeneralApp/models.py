# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class EmergencyContact(models.Model):
    contact = models.IntegerField(blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.country.country_name)+" emergency contact"
