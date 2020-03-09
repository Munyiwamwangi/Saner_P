import copy
import re
import time

import schedule
# from crontab import CronTab
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from leave_management.views import salesforcelogin
from users.models import CustomUser

from .models import Employee


<<<<<<< HEAD
def landing(request):
    current_user = request.user
    context={
        'current_user':current_user,
    }
    return render (request, 'users/landing.html', context)
=======
    
>>>>>>> Integrating the login templated
    
#QUERRY [Employee details from postgress]
@login_required
def employee_directory(request):
    current_user = request.user
    print(current_user.email)
    # print(current_user.Id)
    employee = Employee.objects.all().order_by('email')
    print(employee.count())
    context = {}
    context['employee'] = employee
    return render(request, 'employee/employee_directoryhtml.html', context)


# @login_required
def user_directory(request):
    current_user = request.user
    employee = CustomUser.objects.all()
    context = {}
    context['employee'] = employee
    return render(request, 'employee/employee_directoryhtml.html', context)


def employee_profile(request):
    current_user = request.user
    employee = Employee.objects.get(Id  = current_user.salesforceid)
    context={
        'employee':employee
    }
    return render(request, 'employee/profile.html', context)


# Inserting Employee details SOQL
# @login_required
def populate_postgres(request):
    sf = salesforcelogin()
    managers_list = []
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
        managers_list.append(employee_data['Line_Manager__c'])
        for i in managers_list:
            if i == employee_data['Line_Manager__c']:

                # emp = sf.Employee__c.get('003e0000003GuNXAA0')

                Id = employee_data["Id"]
                manager = employee_data['Name']
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

                # Inserting employees to database

                Employee.objects.update_or_create(Id=Id,
                                            defaults={
                                            'Employee_Full_Name':Name,
                                            'Line_Manager':manager,
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



# Refresh Employee details from SF to PGres
def refresh_employees():
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
        "IsDeleted from Employee__c WHERE CreatedDate = TODAY OR LastModifiedDate = TODAY")
        
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

        # Inserting them to database 
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

    # print(context)
    # print('********************  list end ****************** list end **********************************************')

    # return render(request, 'employee/employee_directory.html', context)
    return JsonResponse(data, safe=False)

# schedule.every(1).day.do(refresh_employees)

# while True:
#     schedule.run_pending()
#     time.sleep(1)