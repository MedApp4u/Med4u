from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from .choices import * 
from phonenumber_field.modelfields import PhoneNumberField
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#Create your models here.

class Profile(AbstractUser):
  dob=models.DateField(null=True, blank=True)
  address=models.TextField(max_length=300, null=True, blank=True)
  phone_number=PhoneNumberField(null=True, blank=True)
  blood_group=models.CharField(max_length=5,choices=BLOOD_GROUP_CHOICES, null=True, blank=True)
  gender=models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True)
  profile_pic = models.ImageField(upload_to="profile", blank=True)

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
