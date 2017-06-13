from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

#Create your models here.

class Profile(AbstractUser):
  dob=models.DateField()
  address=models.TextField(max_length=300)
  mobile_no=models.BigIntegerField(validators=[MaxValueValidator(9999999999)])
  blood_group=models.CharField(max_length=5)
  gender=models.CharField(max_length=1)
  profile_pic=models.ImageField()
  def __str__(self):
    return self.username
