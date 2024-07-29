from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Settings)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
