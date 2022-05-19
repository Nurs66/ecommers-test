from django.db import models
from apps.employees.models import Employee


class TradePoint(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,
        related_name='trade_points',
    )

    def __str__(self):
        return f"{self.title} -- {self.employee.name}"

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Trade point'
        verbose_name_plural = 'Trade points'
