from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from main.models import Organization, Service, Patient
def index(request):
    
    Services = Service.objects.all()
    Organizations = Organization.objects.filter(organization_type= "Hospital")
    context = {'Services': Services, 'Organizations': Organizations}
    return render(request, 'index.html', context)
