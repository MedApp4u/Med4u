from django.db import models

class Symptom(models.Model):
    symptom_name = models.CharField(max_length=1000)
    body_parts = models.ManyToManyField(Bodypart)
    # Disease


class Insurance(models.Model):
    insurance_plan= models.CharField(max_length=500)
    expiry date = models.DateField
    start_date= models.DateField
    # User_id


class Bodypart(models.Model):
    bodypart= {
                'head':'head',
                'middle':'neck, chest or stomach'
                'down': 'thighs and legs'
    }