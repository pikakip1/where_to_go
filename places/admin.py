from django.contrib import admin
from .models import Place, PlaceImg


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PlaceImg)
class PlaceImgAdmin(admin.ModelAdmin):
    list_display = ['location_name']
