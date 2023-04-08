from django.db import models
from authentification.models import *

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

        
class Service(TimespantedModel):
    
    SERVICE_TYPE=(
        ("Health_care", "Health care service"),
        ("Health_insurance", "Health Insurance service"),
        ("Emmergency_support", "Emmergency support"),
        ("Aid", "Aid"),
        ("Other", "Other")
    )

    id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=40)
    service_description = models.TextField(blank=True) 
    service_type = models.CharField(default="Health_care", max_length=45, choices=SERVICE_TYPE, blank=True, null=True)  
    objects = models.Manager()
    
class Domain(TimespantedModel):
    id=models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=40)
    domain_description = models.TextField(blank=True)
    objects = models.Manager()
    
class Organization(TimespantedModel):
    ORGANIZATION_TYPE=(
        ("Hospital", "Hospital"),
        ("Clinic", "Clinic"),
        ("Drugstore", "Drugstore"),
        ("Insurance", "Insurance Institute"),
        ("Other", "Other")
    )
    id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    organization_type = models.CharField(default="Hospital", choices=ORGANIZATION_TYPE, max_length=40)
    
    avenue = models.CharField(max_length=25)
    township = models.CharField(max_length=30)
    town=models.CharField(max_length=25)
    country = models.CharField(max_length=40)
    
    longitute = models.CharField(max_length=25)
    latitude = models.CharField(max_length=25)
    
    email = models.EmailField(),
    phone1 = models.CharField(),
    phone2 = models.CharField(),
    
    domain = models.ForeignKey(Domain,  null=False, blank=False, on_delete=models.DO_NOTHING, related_name="organized_domain",)
    user = models.OneToOneField(Users, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="oganisation_admin_user")
    
    objects = models.Manager()
    
    def __str__(self):
       return self.organization_name
    
       
class Patient(TimespantedModel):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    gender=models.CharField(max_length=20)
    
    avenue = models.CharField(max_length=25)
    township = models.CharField(max_length=30)
    town=models.CharField(max_length=25)
    country = models.CharField(max_length=40)
    
    longitute = models.CharField(max_length=25)
    latitude = models.CharField(max_length=25)
    
    email = models.EmailField(),
    phone1 = models.CharField(),
    phone2 = models.CharField(),
    
    profile_pic = models.FileField()
    
    objects = models.Manager()



    
@receiver(post_save, sender=Users)
def create_user_profile(sender,instance, created, **kwargs):
    if created:
        if instance.user_type==2:
            Organization.objects.create(admin=instance)
        # if instance.user_type==2:
        #     CompteInvest.objects.create(admin=instance)
       
         
@receiver(post_save, sender=Users)
def save_user_profile(sender,instance, **kwargs):
    if instance.user_type==2:
        instance.Organizations.save()
    # if instance.user_type==2:
    #     instance.compteinvests.save()