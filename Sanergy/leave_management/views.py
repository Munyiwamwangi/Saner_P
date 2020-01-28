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
