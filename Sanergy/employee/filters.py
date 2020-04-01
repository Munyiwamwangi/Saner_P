import django_filters
from django import forms

from .models import Employee
from leave_management.models import  SanergyDepartment, SanergyDepartmentUnit

class EmployeeFilter(django_filters.FilterSet):
    Employee_First_Name = django_filters.CharFilter(lookup_expr='icontains')
    Primary_Phone = django_filters.CharFilter(lookup_expr='icontains')
    Joined_Date = django_filters.NumberFilter(lookup_expr='year__gt')
    Sanergy_Department_Unit = django_filters.CharFilter()
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Employee.objects.all(),
    #     widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Employee
        fields = ['Employee_First_Name', 'Employee_Last_Name', 'Sanergy_Department_Unit','Joined_Date', ]
