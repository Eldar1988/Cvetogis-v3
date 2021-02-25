from django.contrib import admin

from .models import City, DeliveryBranch


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('slug', 'order')


@admin.register(DeliveryBranch)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city', 'order')
    list_editable = ('price', 'city', 'order')
    list_filter = ('city',)
    search_fields = ('title',)

    save_as = True
    save_on_top = True
