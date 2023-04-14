from django import forms
from main.models import Organization, Patient

class IdentityCheckForm(forms.Form):
    BOOL_CHOICES = [(True, 'Patient'), (False, 'Organization')]
    choice = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES),
        required=False
    )

    
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields = ('avenue', 'township', 'country')
        