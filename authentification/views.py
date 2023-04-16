from django.shortcuts import render

# Create your views here.
def login(request):
    
    return render(request, "authentification/login.html")
    
   
    

# def doLogin(request):
#     if request.method != "POST":
#         return HttpResponse("method not allow")
#     else :
#         user=EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
#         if user != None:
#             login(request, user)
#             if user.user_type=="1":
#                 return HttpResponseRedirect(reverse('admin_dashbord'))
#             else :
#                 return HttpResponseRedirect(reverse('user_dash'))
 
#         else :
#             messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
#             return HttpResponseRedirect(reverse('login'))

def doLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def userDetails(request):
    if request.user != None :
        return HttpResponse("Email : " + request.POST.get("email") + " Password : " + request.POST.get("password"))
    else :
        return HttpResponse("Please Login First")