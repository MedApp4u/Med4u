from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	dob=models.DateField()
	address=models.TextField(max_length=300)
	mobile_no=models.BigIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
	blood_group=models.CharField(max_length=5)
	gender=models.CharField(max_length=1)

