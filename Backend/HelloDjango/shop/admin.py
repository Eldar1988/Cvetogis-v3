from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import City, DeliveryBranch, Sort, Reason, Image, Product, PresentCategory, Recommendation, People, Seller


admin.site.register(PresentCategory)
admin.site.register(Recommendation)
admin.site.register(Seller)


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


@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('slug', 'order')
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('slug', 'order')
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order', 'icon')
    list_editable = ('slug', 'order', 'icon')
    search_fields = ('title',)

    save_as = True
    save_on_top = True


class ImagesInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'get_image', 'title', 'price', 'old_price', 'future', 'flower', 'show_on_home_page',
        'bouquet', 'in_the_box', 'set', 'present', 'public', 'order', 'slug', 'seller')
    list_editable = (
        'price', 'old_price', 'future', 'flower', 'show_on_home_page', 'bouquet', 'in_the_box', 'set',
        'public', 'order', 'present',)
    search_fields = ('title',)
    list_display_links = ('get_image', 'title')
    list_filter = (
        'future', 'flower', 'show_on_home_page', 'bouquet', 'in_the_box', 'set', 'present', 'public', 'sort', 'reasons',
        'cities', 'seller')
    save_as = True
    save_on_top = True
    list_per_page = 12
    inlines = [ImagesInline]

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height=50')

    get_image.short_description = 'Фото'

