from django.contrib import admin

from .models import UserType, UserProfile

admin.site.register(UserType)
admin.site.register(UserProfile)