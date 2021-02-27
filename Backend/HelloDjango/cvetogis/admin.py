from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Slider, PrivacyPolicy, PublicOffer, ShippingAndPayment, AboutInfo, Testimonial

admin.site.register(PrivacyPolicy)
admin.site.register(PublicOffer)
admin.site.register(ShippingAndPayment)
admin.site.register(AboutInfo)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'text', 'button_text', 'order')
    list_editable = ('title', 'text', 'button_text', 'order')
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height=50')

    get_image.short_description = 'Фото'


@admin.register(Testimonial)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'public', 'pub_date')
    list_editable = ('name', 'public')
    list_filter = ('public', 'pub_date')
    save_as = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height=50')

    get_image.short_description = 'Фото'
