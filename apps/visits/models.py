from django.db import models
from apps.trade_points.models import TradePoint


class Visit(models.Model):
    create_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Create at'
    )
    trade_point = models.ForeignKey(
        TradePoint, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='visits',
        verbose_name='Trade point'
    )
    latitude = models.FloatField(
        verbose_name='Latitude'
    )
    longitude = models.FloatField(
        verbose_name='Longitude'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Visit'
        verbose_name_plural = 'Visit'
