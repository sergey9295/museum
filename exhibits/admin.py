from django.contrib import admin
from django.contrib.auth.models import AbstractUser, Group
from .models import Exhibit, ExhibitItem


@admin.register(Exhibit)
class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor', 'is_open')
    search_fields = ('name', 'floor')

@admin.register(ExhibitItem)
class ExhibitItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'exhibit', 'status')
    search_fields = ('name', 'status')
    list_filter = ('status',)
