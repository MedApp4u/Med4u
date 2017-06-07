# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Disease(models.Model):
    disease_name=models.CharField(max_length=20)
    disease_id=models.AutoField(primary_key=True)
    symptom=models.ForeignKey(Symptom, on_delete=models.CASCADE)
    procedure=models.ForeignKey(Procedure, on_delete=models.CASCADE)
    medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE)
