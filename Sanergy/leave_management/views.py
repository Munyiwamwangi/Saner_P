from django.http import JsonResponse
from django.shortcuts import render

from users.utils import salesforcelogin


def leave_application(request):
    return render(request, 'users/login.html')


def leave_types(request):
    sf = salesforcelogin()
    data = sf.query(
        "SELECT Id, name,Leave_Type__c, Leave_Group__c from Leave_Entitlement_Type_Config__c where Year__c=2019")

    return JsonResponse(data)
  

def request_leave(request):
    sf = salesforcelogin()
    data = sf.Leave_Entitlement_Type_Config__c.create(
        {'Accrue__c': 'Start Month', 'Leave_Group__c': 'aJ87E0000004CAu', 'Leave_Type__c': 'Annual Leave', 'Total_No_of_Leave_Days__c': '5', 'Year__c': '2020'})

    return JsonResponse(data)


def approve_leave(request):
    return render(request, 'leave_management/approve.html')
