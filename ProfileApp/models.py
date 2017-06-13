from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

#Create your models here.

class Profile(AbstractUser):
  dob=models.DateField(null=True)
  address=models.TextField(max_length=300, null=True)
  mobile_no=models.BigIntegerField(validators=[MaxValueValidator(9999999999)], null=True)
  blood_group=models.CharField(max_length=5, null=True)
  gender=models.CharField(max_length=1, null=True)
  profile_pic=models.ImageField(upload_to="profile", null=True)
  def __str__(self):
    return self.username
