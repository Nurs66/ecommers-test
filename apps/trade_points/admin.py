from django.contrib import admin
from apps.trade_points.models import TradePoint


@admin.register(TradePoint)
class TradePointAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'employee',
    )
    search_fields = (
        'title',
    )
