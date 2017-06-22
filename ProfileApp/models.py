from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from .choices import * 
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#Create your models here.

class Profile(AbstractUser):
  dob=models.DateField(null=True)
  address=models.TextField(max_length=300, null=True)
  phone_number=PhoneNumberField()
  blood_group=models.CharField(max_length=5,choices=BLOOD_GROUP_CHOICES, null=True)
  gender=models.CharField(max_length=1,choices=SEX_CHOICES, null=True)
  profile_pic=models.ImageField(upload_to="profile", null=True)

  def __str__(self):
    return self.username

  def __iter__(self):
    return self

  def next(self):
    raise StopIteration
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
