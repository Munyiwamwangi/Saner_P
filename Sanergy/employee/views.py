from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from pandas.io.json import json_normalize

from leave_management.views import salesforcelogin

from .dbcon import postgressConnection


# Employee details SOQL
@login_required
def employee_details(request):
    sf = salesforcelogin()
    data = sf.bulk.Employee__c.query(
        "SELECT Id,"
        "Line_Manager__c,"
        "HR_Employee_ID__c,"
        "Employee_Active__c,"
        "Employee_First_Name__c,"
        "name,Work_Email__c, IsDeleted  from Employee__c LIMIT 2")
    normalized_data = json_normalize(data, max_level=0, record_prefix='Prefix.')
    print(type(normalized_data))
    print(type(data[0]))

    context = {
        'data': data
    }

    # looping through data list to access every object
    for employee_data in data:
        for key, value in employee_data.items():
            # print(key[1])
            print('{}: {}'.format(key, value))

        # Accessing values only
        k = employee_data.keys()
        for i in k:
            print(employee_data[i])

        # keys only, not tested though
        first_dictionary = data[0]
        k = first_dictionary.keys()
        for i in k:
            print(first_dictionary[i])

    return render(request, 'leave_templates/employee_directory.html', context)
    # return JsonResponse(context, status=200)


def psqlEmployeeDetails(request):
    connection = postgressConnection()
    cursor = connection.cursor()
    data = "select * from employee_employee"

    cursor.execute(data)
    employee_records = cursor.fetchall()

    return JsonResponse(employee_records, safe=False)
