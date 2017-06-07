from django.db import models

class Symptom(models.Model):
    symptom_name = models.CharField(max_length=1000)
    body_parts = models.ManyToManyField(Bodypart)
    medicines = models.ManyToManyField(Medicine)
    # Disease
    def __str__(self):
        return self.symptom_name

class Insurance(models.Model):
    insurance_plan= models.CharField(max_length=500)
    expiry date = models.DateField
    start_date= models.DateField
    # User_id
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.insurance_plan

class Bodypart(models.Model):
    bodypart= {
                'head':'head',
                'middle':'neck, chest or stomach'
                'down': 'thighs and legs'
            }
    medicines = models.ManyToManyField(Medicine)


    def __str__(self):
        return self.bodypart