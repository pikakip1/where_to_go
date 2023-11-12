from django.contrib import admin
from .models import Place, PlaceImg


class PlaceImgInline(admin.TabularInline):
    model = PlaceImg
    extra = 1


@admin.register(PlaceImg)
class PlaceImgAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'image']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImgInline]





