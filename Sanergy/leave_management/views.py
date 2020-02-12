<<<<<<< HEAD
import io
import json
import sys

import pandas
import simplejson as json
from django.conf.urls import include, url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template import Context, RequestContext, Template
from django.views import generic
from pandas.io.json import json_normalize
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from simple_salesforce import Salesforce, SalesforceLogin, SFType

from .serializers import (EmploymentTermsSerializer,
                          LeaveClassDetailsSerializer, LeaveSerializer)
from users.utils import salesforcelogin


# def salesforcelogin():
#     return Salesforce(
#         username='domnick.kamya@saner.gy.ffa',
#         password='Sanergy123',
#         security_token='RolR1FqVokyPBjREIoBDq21j',
#         domain='test'
#     )

=======
from django.http import JsonResponse
from django.shortcuts import render

from users.utils import salesforcelogin


>>>>>>> 30678670a8974b921c88559373c91151852d9f57
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
