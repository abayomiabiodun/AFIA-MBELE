from django import forms
from main.models import Organization, Patient

class IdentityCheckForm(forms.Form):
    BOOL_CHOICES = [(True, 'Patient'), (False, 'Organization')]
    choice = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES),
        required=False
    )

    
class PatientForm(forms.ModelForm):
    
    First_name = forms.CharField(max_length=100)
    Last_name = forms.CharField(max_length=100)
    class Meta:
        model=Patient
        fields = ('First_name', 'Last_name', 'avenue', 'township', 'country')

class UserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
        attrs={
            "class":"form-control"
        }),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
        attrs={
            "class":"form-control"
        }
    ))
    password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ))
    