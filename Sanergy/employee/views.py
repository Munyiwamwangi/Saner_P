<<<<<<< HEAD
# import psycopg2
import json
=======
#function to populate and update postgres
import copy
import re
>>>>>>> 30678670a8974b921c88559373c91151852d9f57

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

<<<<<<< HEAD
from employee.models import Employee
=======
>>>>>>> 30678670a8974b921c88559373c91151852d9f57
from leave_management.views import salesforcelogin

from .dbcon import postgressConnection
from .models import Employee

<<<<<<< HEAD
# Employee details SOQL query
# @login_required
=======

def landing(request):
    return render (request, 'users/landing.html')
    
#employee querry from postgress
>>>>>>> 30678670a8974b921c88559373c91151852d9f57
def employee_details(request):
    employee = Employee.objects.all()
    context={}
    context['employee'] = employee
    return render(request, 'leave_templates/employee_directoryhtml.html', context)


def psqlEmployeeDetails(request):
    connection = postgressConnection()
    cursor = connection.cursor()
    data = "select * from employee_employee"
    cursor.execute(data)
    employee_records = cursor.fetchall()
    return JsonResponse(employee_records, safe=False)


 #Employee details SOQL
# @login_required
def populate_postgres(request):
    sf = salesforcelogin()
    data = sf.bulk.Employee__c.query(
        "SELECT Id,"
        "Line_Manager__c,"
        "HR_Employee_ID__c,"
        "Employee_Active__c,"
        "Employee_First_Name__c,"
<<<<<<< HEAD
        "name,Work_Email__c, IsDeleted  from Employee__c LIMIT 10")
    normalized_data = json_normalize(data, max_level=0, record_prefix='Prefix.')
    print(type(normalized_data))
    print(type(data[0]))

    context = {
        'data': data
    }


def psqlEmployeeDetails(request):
    connection = postgressConnection()
    cursor = connection.cursor()
    data = "select * from employee_employee"

    cursor.execute(data)
    employee_records = cursor.fetchall()

    return JsonResponse(employee_records, safe=False)
=======
        "name,Work_Email__c, IsDeleted  from Employee__c ")
    context = {
        'data': data
    }
    for employee_data in data:
        Id  = employee_data["Id"]
        Line_Manager__c = employee_data["Line_Manager__c"]
        HR_Employee_ID__c = employee_data[ "HR_Employee_ID__c"]
        Employee_Active__c = employee_data["Employee_Active__c"]
        Employee_First_Name__c = employee_data["Employee_First_Name__c"]
        Name = employee_data["Name"]
        Work_Email__c = employee_data["Work_Email__c"]
        IsDeleted = employee_data["IsDeleted"]

        #map these employees to database
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

    return render(request, 'leave_templates/employee_directory.html', context)
    # return JsonResponse(data, safe=False)
>>>>>>> 30678670a8974b921c88559373c91151852d9f57
