from django.shortcuts import render
from django.http import HttpResponse

from main.models import Organization, Service, Patient

from formtools.wizard.views import SessionWizardView
from main.forms import IdentityCheckForm, PatientForm
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
    form_list = [IdentityCheckForm]
    template_name = 'main/registration.html'
    condition_dict={'1': show_organization_form}
    def done(self, form_list,**kwargs):
        check_form = form_list[0]
        return HttpResponse("Form submitted successfully")

