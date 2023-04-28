from django import forms
from main.models import Organization, Patient
from django.contrib.auth.forms import UserCreationForm
from authentification.models import Users

class IdentityCheckForm(forms.Form):
    BOOL_CHOICES = [(True, 'Patient'), (False, 'Organization')]
    choice = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES),
        label="Type d'utilisateur",
        required=False
    )

    
class PatientForm(forms.Form):
    
    First_name = forms.CharField(max_length=100,                  
            widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    Last_name = forms.CharField(max_length=100,
            widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        ))
    
        
class OrgnizationForm(forms.Form):
    
    First_name = forms.CharField(max_length=100)
    Last_name = forms.CharField(max_length=100)
    class Meta:
        model=Organization
        fields = ('First_name', 'Last_name', 'avenue', 'township', 'country')

class SignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    

    class Meta:
        model = Users
        fields = {'username', 'email', 'password', 'user_type'}
    