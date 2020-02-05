# import psycopg2
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from pandas.io.json import json_normalize
from simple_salesforce import Salesforce, SalesforceLogin, SFType

from employee.models import Employee
from leave_management.views import salesforcelogin

from .dbcon import postgressConnection

# Employee details SOQL query
# @login_required
def employee_details(request):
    sf = salesforcelogin()
    data = sf.bulk.Employee__c.query(
        "SELECT Id,"
        "Line_Manager__c,"
        "HR_Employee_ID__c,"
        "Employee_Active__c,"
        "Employee_First_Name__c,"
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
