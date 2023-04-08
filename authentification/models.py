from django.db import models
from django.contrib.auth.models import AbstractUser
class TimespantedModel(models.Model) :
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta :
        abstract = True

class Users(AbstractUser):
    user_type_data = (
                        (1,"Admin"), 
                        (2,"Organization Admin"), 
                        (3,"Patients"), 
                        (4, "Doctors"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)