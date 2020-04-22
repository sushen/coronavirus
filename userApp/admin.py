from django.contrib import admin

# Register your models here.

from userApp.models import UserProfile

admin.site.register(UserProfile)