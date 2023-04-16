from django.shortcuts import render
from django.http import HttpResponse

from main.models import Organization, Service, Patient

from formtools.wizard.views import SessionWizardView
from main.forms import IdentityCheckForm, PatientForm,UserForm
# Create your views here.

def list_hospital(request):
    
    Organizations = Organization.objects.filter(organization_type= "Hospital")
    context = {'Organizations': Organizations}
    return render(request, 'main/liste_hopital.html', context)


def show_organization_form(wizard):
    # try to get the cleaned data of step 1
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    # check if the field ``choice`` was checked.
    return cleaned_data.get('choice')

class RegistrationWizardView(SessionWizardView):
    form_list = [IdentityCheckForm, PatientForm, UserForm]
    template_name = 'main/registration.html'

    def done(self, form_list,**kwargs):
        print(form_list)
        return HttpResponse("Form submitted successfully")

