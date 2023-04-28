from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth import login as auth_login
from django.contrib import messages
from authentification.forms import *


# Create your views here.


# Display the login page
def showlogin(request):
    form = LoginForm()
    context = {"form":form}
    return render(request, "authentification/login.html", context)   

# login process

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username, password= password)
            
            if user is not None:
                login(request, user)
                if user.user_type=="Admin":
                    return HttpResponseRedirect(reverse('admin:index'));
                else:
                    return HttpResponseRedirect(reverse('Dashboardhospital'))
            else:
                msg = 'invalide credentials'
                return HttpResponse("Invalid credential")
        else :
            msg = 'error validating form'
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, "authentification/login.html", {'form': form, 'msg' : msg}) 

# logout process
def doLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


# user registration process : request

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return HttpResponseRedirect(reverse('login'))
        else : 
            msg = 'form is not valid'
    else:
        form = SignupForm()
    return render(request, "authentification/login.html", {'form': form, 'msg' : msg}) 


