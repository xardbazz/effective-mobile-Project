from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)

# Register your models here.
