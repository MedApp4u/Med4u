from django.db import models
from GeneralApp.models import User


# Create your models here.

class Measurement(models.Model):
    blood_pressure = models.CharField(max_length=30)
    blood_sugar = models.CharField(max_length=30)
    cholesterol = models.CharField(max_length=30)
    height = models.FloatField()
    weight = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Procedure(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    possible_complication = models.CharField(max_length=300)
    image = models.FileField()
    video = models.FileField()
    bodypart = models.ManyToManyField(Bodypart)
    symptom = models.ManyToManyField(Symptom)
    medicine = models.ManyToManyField(Medicine)

    def __str__(self):
        return self.name



