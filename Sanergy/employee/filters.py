from .models import Employee
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['Employee_First_Name', 'Employee_Last_Name', 'Sanergy_Department_Unit', ]