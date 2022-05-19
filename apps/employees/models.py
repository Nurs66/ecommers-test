from django.db import models


class Employee(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Name'
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name='Phone number'
    )

    def __str__(self):
        return f"{self.name} -- {self.phone_number}"

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
