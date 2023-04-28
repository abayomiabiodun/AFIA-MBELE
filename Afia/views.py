from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from main.models import Organization, Service


# home page view
def index(request):
    
    Services = Service.objects.all()
    Organizations = Organization.objects.filter(organization_type= "Hospital")
    context = {'Services': Services, 'Organizations': Organizations}
    return render(request, 'index.html', context)

# main portal - hospital list
def list_hospital(request):
    
    Organizations = Organization.objects.filter(organization_type= "Hospital")
    context = {'Organizations': Organizations}
    return render(request, 'main/liste_hopital.html', context)

# main portal - health insurance provider
def provider(request):
    Organizations = Organization.objects.filter(organization_type= "Insurance institution")
    context = {'Organizations': Organizations}
    return render(request, 'main/liste_providers.html', context)