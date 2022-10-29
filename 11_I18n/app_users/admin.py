from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'date_of_birth', 'number_phone',)
    list_filter = ('user', 'city')


