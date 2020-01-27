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
from django.shortcuts import render
from simple_salesforce import Salesforce
from django.http import HttpResponse
from .serializers import LeaveSerializer
from django.http import JsonResponse
import json

def salesforceLogin():
    return Salesforce(
        username='domnick.kamya@saner.gy.ffa',
        password='Sanergy123',
        security_token='RolR1FqVokyPBjREIoBDq21j',
        domain='test'
    )

def salesforceLogin():
    return Salesforce(
        username='domnick.kamya@saner.gy.ffa',
        password='Sanergy123',
        security_token='RolR1FqVokyPBjREIoBDq21j',
        domain='test'
    )


def leave_types(request):
    sf = salesforceLogin()
    data = sf.query(
        "SELECT Id, name,Leave_Type__c, Leave_Group__c from Leave_Entitlement_Type_Config__c where Year__c=2019")

    return JsonResponse(data)


def request_leave(request):
    sf = salesforceLogin()
    data = sf.Leave_Entitlement_Type_Config__c.create(
        {'Accrue__c': 'Start Month', 'Leave_Group__c': 'aJ87E0000004CAu', 'Leave_Type__c': 'Annual Leave', 'Total_No_of_Leave_Days__c': '5', 'Year__c': '2020'})

    return JsonResponse(data)


def approve_leave(request):
    return render(request, 'leave_management/approve.html')
