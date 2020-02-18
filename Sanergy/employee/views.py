import copy
import re

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from leave_management.views import salesforcelogin
from .models import Employee

def landing(request):
    user = request.user
    return render(request, 'registration/landing.html')



# employee querry from postgress
def employee_details(request):
    employee = Employee.objects.all()
    context = {}
    context['employee'] = employee
    return render(request, 'employee/employee_directoryhtml.html', context)


def employee_profile(request):
    employee = Employee.objects.all()
    context={
        'employee':employee
    }
    return render(request, 'employee/profile.html', context)

def employee_profile(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee
    }
    return render(request, 'employee/profile.html', context)

# Employee details SOQL
# @login_required
def populate_postgres(request):
    sf = salesforcelogin()
    data = sf.bulk.Employee__c.query(
        "SELECT Id,"
        "Line_Manager__c,"
        "HR_Employee_ID__c,"
        "Employee_Active__c,"
        "Employee_First_Name__c,"
        "name,Work_Email__c, IsDeleted  from Employee__c ")
    context = {
        'data': data
    }
    for employee_data in data:
        Id = employee_data["Id"]
        Line_Manager__c = employee_data["Line_Manager__c"]
        HR_Employee_ID__c = employee_data["HR_Employee_ID__c"]
        Employee_Active__c = employee_data["Employee_Active__c"]
        Employee_First_Name__c = employee_data["Employee_First_Name__c"]
        Name = employee_data["Name"]
        Work_Email__c = employee_data["Work_Email__c"]
        IsDeleted = employee_data["IsDeleted"]

        Employee.objects.update_or_create(Id=Id,
                                    Line_Manager=Line_Manager__c,
                                    HR_Employee_ID=HR_Employee_ID__c,
                                    Employee_Active=Employee_Active__c,
                                    Employee_First_Name=Employee_First_Name__c,
                                    Employee_Full_Name=Name,
                                    IsDeleted=IsDeleted,
                                    email=Work_Email__c)

    employee = Employee.objects.all()
    for item in employee:
        context['employee'] = employee
    return render(request, 'employee/employee_directory.html', context)
    # return JsonResponse(data, safe=False)

def create_custom_user(request):
    employee = Employee.objects.filter(email__isnull=False).exclude(Id__isnull=True)
    context = {
        'employee': employee
    }
    for field in employee:
        print(field.Employee_Full_Name)
    return render(request, 'employee/employee_directory.html', context)
