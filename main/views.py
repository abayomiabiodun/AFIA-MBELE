from django.shortcuts import render
from main.models import Organization, Service, Patient
# Create your views here.

def list_hospital(request):
    
    Organizations = Organization.objects.filter(organization_type= "Hospital")
    context = {'Organizations': Organizations}
    return render(request, 'main/liste_hopital.html', context)
