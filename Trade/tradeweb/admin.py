from django.contrib import admin

# Register your models here.
from tradeweb.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']
    pass