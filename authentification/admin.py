from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import Users

# class UserModel(UserAdmin):
#     pass

# admin.site.register(Users,UserModel)


admin.site.register(Users)