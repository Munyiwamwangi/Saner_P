import copy
import re

from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from leave_management.views import salesforcelogin

from .models import Employee


def landing(request):
    return render (request, 'users/landing.html')
    
    
#employee querry from postgress
@login_required
def employee_details(request):
    current_user = request.user
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
        "name,Work_Email__c, Department__c,"
        "Sanergy_Department__c,"
        "Sanergy_Department_Unit__c,"
        "Talent_Partner__c,"
        "Team_Lead__c, "
        "IsDeleted from Employee__c")
        
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
        Department__c = employee_data["Department__c"]
        Sanergy_Department__c = employee_data['Sanergy_Department__c']
        Sanergy_Department_Unit__c = employee_data['Sanergy_Department_Unit__c']
        Talent_Partner__c = employee_data['Talent_Partner__c']
        Team_Lead__c = employee_data['Team_Lead__c']
        IsDeleted = employee_data["IsDeleted"]

        Employee.objects.update_or_create(Id=Id,
                                    defaults={
                                    'Employee_Full_Name':Name,
                                    'Line_Manager':Line_Manager__c,
                                    'email':Work_Email__c,
                                    'HR_Employee_ID':HR_Employee_ID__c,
                                    'Employee_Active':Employee_Active__c,
                                    'Employee_First_Name':Employee_First_Name__c,
                                    'IsDeleted':IsDeleted,
                                    'Employee_Department':Department__c,
                                    'Sanergy_Department':Sanergy_Department__c,
                                    'Sanergy_Department_Unit':Sanergy_Department_Unit__c,
                                    'Talent_Partner':Talent_Partner__c,
                                    'Team_Lead':Team_Lead__c,
                                    })

    employee = Employee.objects.all()
    print(employee.count())
    for item in employee:
        context['employee'] = employee

    return render(request, 'employee/employee_directory.html', context)
    # return JsonResponse(data, safe=False)


# Refresh Employee details SOQL 

def refresh_employees(request):
    sf = salesforcelogin()
    data = sf.bulk.Employee__c.query(
        "SELECT Id,"
        "Line_Manager__c,"
        "HR_Employee_ID__c,"
        "Employee_Active__c,"
        "Employee_First_Name__c,"
        "name,Work_Email__c, Department__c,"
        "Sanergy_Department__c,"
        "Sanergy_Department_Unit__c,"
        "Talent_Partner__c,"
        "Team_Lead__c, "
        "IsDeleted from Employee__c WHERE CreatedDate = TODAY OR LastModifiedDate = TODAY ")
    context = {
        'employee': employee
    }
    for employee_data in data:
        Id  = employee_data["Id"]
        Line_Manager__c = employee_data["Line_Manager__c"]
        HR_Employee_ID__c = employee_data[ "HR_Employee_ID__c"]
        Employee_Active__c = employee_data["Employee_Active__c"]
        Employee_First_Name__c = employee_data["Employee_First_Name__c"]
        Name = employee_data["Name"]
        Work_Email__c = employee_data["Work_Email__c"]
        Department__c = employee_data["Department__c"]
        Sanergy_Department__c = employee_data['Sanergy_Department__c']
        Sanergy_Department_Unit__c = employee_data['Sanergy_Department_Unit__c']
        Talent_Partner__c = employee_data['Talent_Partner__c']
        Team_Lead__c = employee_data['Team_Lead__c']
        IsDeleted = employee_data["IsDeleted"]

        Employee.objects.update_or_create(Id=Id,
                                    defaults={
                                    'Employee_Full_Name':Name,
                                    'Line_Manager':Line_Manager__c,
                                    'email':Work_Email__c,
                                    'HR_Employee_ID':HR_Employee_ID__c,
                                    'Employee_Active':Employee_Active__c,
                                    'Employee_First_Name':Employee_First_Name__c,
                                    'IsDeleted':IsDeleted,
                                    'Employee_Department':Department__c,
                                    'Sanergy_Department':Sanergy_Department__c,
                                    'Sanergy_Department_Unit':Sanergy_Department_Unit__c,
                                    'Talent_Partner':Talent_Partner__c,
                                    'Team_Lead':Team_Lead__c,
                                    })

    employee = Employee.objects.all()
    print(employee.count())
    for item in employee:
        context['employee'] = employee
    return render(request, 'employee/employee_directory.html', context)


def create_custom_user(request):
    employee = Employee.objects.filter(email__isnull=False).exclude(Id__isnull=True)
    context={
        'employee':employee
    }
    for field in employee:
        print(field.Employee_Full_Name)
    return render(request, 'employee/employee_directory.html', context)
