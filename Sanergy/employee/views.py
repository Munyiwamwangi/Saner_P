from django.shortcuts import render
from leave_management.views import salesforceLogin
from simple_salesforce import Salesforce, SalesforceLogin, SFType
from django.http import JsonResponse
from pandas.io.json import json_normalize
from employee.models import Employee
from django.http import HttpResponse
import psycopg2
import json

from .dbcon import postgressConnection


def employeeDetails(request):
    sf = salesforceLogin()
    data = sf.bulk.Employee__c.query(
        "SELECT Employee_First_Name__c,Employee_Last_Name__c,Employee_Middle_Name__c, department__c,	Employment_Status__c,Employee_Role__c,Employee_SF_Account__c,Employment_Start_Date__c,Leave_Group__c, Line_Manager__c,Work_Email__c from Employee__c LIMIT 5 ")
    normalized_data = json_normalize(
        data, max_level=0, record_prefix='Prefix.')
    print(normalized_data)
    print(type(normalized_data))

    return JsonResponse(data, safe=False)


def psqlEmployeeDetails(request):
    connection = postgressConnection()
    cursor = connection.cursor()
    data = "select * from employee_employee"

    cursor.execute(data)
    employee_records = cursor.fetchall()

    return JsonResponse(employee_records, safe=False)

