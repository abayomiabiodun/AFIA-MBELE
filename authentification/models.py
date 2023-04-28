from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class TimespantedModel(models.Model) :
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta :
        abstract = True

class CustomerUserManager(BaseUserManager):
    
    def create_user(self, username, email, password,**other_fields):
        
        if not email:
            raise ValueError(_('You must provide an email address'))
        if not username:
            raise ValueError(_('You must provide an username'))
        email = self.normalize_email(email)
        user = self.model(email = email, username=username,**other_fields)
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password,**other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser mut be assigned to is_staff = True'))
    
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser mut be assigned to is_superuser = True'))
        
        return self.create_user(username, email, password, **other_fields)
    
class Users(TimespantedModel, AbstractBaseUser, PermissionsMixin):
    
    class UserTypeData(models.TextChoices):
        ADMIN = "Admin"
        ORGANIZATION = "Organization"
        PATIENT = "Patient"
        DOCTOR = "Doctor"

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=50, unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
 
    user_type = models.CharField(default=UserTypeData.ADMIN, choices=UserTypeData.choices, max_length=25)
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    
    objects = CustomerUserManager()
    
 
    def __str__(self):
        return self.username

    # class Meta:
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'