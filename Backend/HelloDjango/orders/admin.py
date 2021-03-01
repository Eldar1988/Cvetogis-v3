from django.contrib import admin
from .models import CallBack


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ('phone', 'complete', 'date', 'update')
    list_editable = ('complete',)
    list_filter = ('complete', 'date', 'update')
    search_fields = ('phone',)
