from django.shortcuts import render

# Create your views here.

def hopitalDash(request):
    return render(request, "hospital/index.html")
