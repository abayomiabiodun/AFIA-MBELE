from django.db import models
from django.contrib.auth.models import AbstractUser
class TimespantedModel(models.Model) :
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta :
        abstract = True

class Users(AbstractUser):
    user_type_data = (
                        ("Admin","Admin"), 
                        ("Organization Admin","Organization Admin"), 
                        ("Patients","Patients"), 
                        ("Doctors", "Doctors"))
    user_type = models.CharField(default="Admin", choices=user_type_data, max_length=25)