from django.http import JsonResponse
from django.shortcuts import render

from users.utils import salesforcelogin


def leave_application(request):
    return render(request, 'users/login.html')


def Leave_Entitlement_Types(request):
    sf = salesforcelogin()
    leave_type_data = sf.query(
        "SELECT Id,name,Leave_Type__c, Leave_Group__c from Leave_Entitlement_Type_Config__c where Year__c=2019")
    # context = {
    #     'leave_type_data': leave_type_data
    # }
    # # getting every dictionary in the retrieved list of employee dictionaries

    # for leave_types in leave_type_data:
    #     # saving every leave type in postgress
    #     Leave_types.objects.create(Id=Id,
    #                              name=leave_types["name"],
    #                              leave_type=leave_types["Leave_Type__c"],
    #                              leave_group=leave_types["Leave_Group__c"],
    #

    # return HttpResponse('DB ostgreSQL sucessfully populated!')
    return JsonResponse(leave_type_data)
  

def request_leave(request):
    sf = salesforcelogin()
    data = sf.Leave_Entitlement_Type_Config__c.create(
        {'Accrue__c': 'Start Month', 'Leave_Group__c': 'aJ87E0000004CAu', 'Leave_Type__c': 'Annual Leave', 'Total_No_of_Leave_Days__c': '5', 'Year__c': '2020'})
    return JsonResponse(data)


def approve_leave(request):
    return render(request, 'leave_management/approve.html')
