from django.db import models
from authentification.models import *

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CommonData(TimespantedModel):
    
    avenue = models.CharField(max_length=25)
    township = models.CharField(max_length=30)
    town=models.CharField(max_length=25)
    country = models.CharField(max_length=40)
    
    longitute = models.CharField(max_length=25)
    latitude = models.CharField(max_length=25)
    
    email = models.EmailField()
    phone1 = models.CharField(max_length=12)
    phone2 = models.CharField(max_length=12)
    
    class Meta :
        abstract = True


    
class Organization(CommonData):
    class OrganizationType(models.TextChoices):
        HOSPITAL = "Hospital"
        DRUGSTORE = "Drugstore"
        CLINIC = "Clinic"
        DISPENSAIR = "Dispensair"
        INSURANCE = "Insurance institution"
        GOVENMENT = "GOVENMENT"
  
    id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    organization_type = models.CharField(default=OrganizationType.HOSPITAL, choices=OrganizationType.choices, max_length=40)
    
    user = models.OneToOneField(Users, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="oganisation_admin_user")
    
    objects = models.Manager()
    
    def __str__(self):
       return self.organization_name
    
       
class Patient(CommonData):
    
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    gender=models.CharField(max_length=20)
    profile_pic = models.FileField()
    
    objects = models.Manager()

    def __str__(self):
       return self.user
class Service(TimespantedModel):
    
    class ServiceType(models.TextChoices):
        HEALTH_CARE = "Health care service"
        HEALTH_INSURANCE = "Health Insurance service"
        Emergency = "Emmergency support"
        AID = "Aid"
        OTHER = "Other"
  

    id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=40, null=False, blank=False)
    service_description = models.TextField(null=True, blank=True)
    service_type = models.CharField(default=ServiceType.HEALTH_CARE, max_length=45, choices=ServiceType.choices, blank=True, null=True)  
    objects = models.Manager()
    
      
    def __str__(self):
       return self.service_name
