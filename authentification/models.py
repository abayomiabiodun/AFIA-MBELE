from django.db import models
from django.contrib.auth.models import AbstractUser
class TimespantedModel(models.Model) :
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta :
        abstract = True

class Users(AbstractUser):
    class UserTypeData(models.TextChoices):
        ADMIN = "Admin"
        ORGANIZATION = "Organization"
        PATIENT = "Patient"
        DOCTOR = "Doctor"
   
    user_type = models.CharField(default=UserTypeData.ADMIN, choices=UserTypeData.choices, max_length=25)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
