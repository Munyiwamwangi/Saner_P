from django.contrib import admin

from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Id', 'email', 'Employee_Full_Name','Line_Manager')