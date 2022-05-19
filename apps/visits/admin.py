from django.contrib import admin
from apps.visits.models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = (
        'create_at', 'trade_point',
        'latitude', 'longitude',
    )
    search_fields = (
        'trade_point__title',
        'trade_point__employee__name'
    )
