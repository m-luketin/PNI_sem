from django.contrib import admin
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import *

UserAdmin.list_display += ('role',)
UserAdmin.list_filter += ('role',)


class Admin(UserAdmin):
    list_display = ('email',)
    ordering = ('email',)
    
admin.site.register(AppUser, Admin)
admin.site.register(Course)
admin.site.register(AppUserCourse)

