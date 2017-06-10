from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


#Create your models here.

class Profile(AbstractUser):
  dob=models.DateField(null=True)
  address=models.TextField(max_length=300, null=True)
  mobile=models.BigIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)], null=True)
  blood_group=models.CharField(max_length=5, null=True)
  gender=models.CharField(max_length=1, null=True)
  def __str__(self):
    return self.name
