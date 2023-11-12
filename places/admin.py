from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminMixin, SortableAdminBase

from .models import Place, PlaceImg


class PlaceImgInline(SortableStackedInline):
    model = PlaceImg
    extra = 1
    readonly_fields = ('image_preview', )

    def image_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=200,
            height=150,
            )
        )


@admin.register(PlaceImg)
class PlaceImgAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'image']


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImgInline]





