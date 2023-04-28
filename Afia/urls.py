"""Afia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from main.views import RegistrationWizardView as Registration_view

urlpatterns = [
    path('', views.index, name='home'),
    path('hopistals/', views.list_hospital, name='listhospital'),
    path('insurance-provider/', views.provider, name='providers'),
    path('registration/', Registration_view.as_view(), name='registrations'),
    
    
    path('authentification/', include('authentification.urls')),
    path('hospital/', include('hospital.urls')),
    path('portal/', include('main.urls')),
    path('admin/', admin.site.urls),
    
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), # Django 
   
]
