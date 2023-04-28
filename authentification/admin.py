from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import Users

class UserModel(UserAdmin):
    
    search_fields =('username', 'email',)
    
    ordering = ('-created_at',)
    
    list_display=('username', 'email', 'is_active', 'is_staff', 'user_type')
    
    fieldsets = (
        (None, {'fields' : ('username', 'email',)}),
        ('Permissions',{'fields' : ('is_staff', 'is_active')}),
        ('Customization',{'fields' : ('user_type',)}),
        )


        
admin.site.register(Users, UserModel)


# admin.site.register(Users)