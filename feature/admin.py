from django.contrib import admin
from django.contrib.admin.sites import site
from django.db import models
from feature.models import login
# Register your models here.
class registration(admin.ModelAdmin):
    list_display=("username","password")

admin.site.register(login,registration)