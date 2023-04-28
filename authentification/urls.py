from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.showlogin, name='login'),
    path('login/', views.login_view, name="dologin"),
    path('lagout/', views.doLogout, name="logout"),
    
   
]