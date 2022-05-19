from django.contrib import admin
from apps.employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'phone_number',
    )
    search_fields = (
        'name',
    )
