from django.db import models

# Create your models here.
class Disease(models.Model):
    disease_name=models.CharField(max_length=20)
    disease_id=models.AutoField(primary_key=True)
    user=models.ManyToManyField(User)
    bodypart=models.ManyToManyField(Bodypart)
    symptom=models.ManyToManyField(Symptom)
    procedure=models.ManyToManyField(Procedure)
    medicine=models.ManyToManyField(Medicine)

    def __str__(self):
    	return self.disease_name