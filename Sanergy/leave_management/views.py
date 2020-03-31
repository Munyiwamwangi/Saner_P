import datetime
import time
from datetime import datetime
import pandas as pd
import numpy as np
# import schedule


from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.models import Employee
from users.utils import salesforcelogin, postgressConnection

from .forms import LeaveApplicationForm
from .models import (EmployeeLeaveRequest, Leave_Entitlement_Type,
                     LeaveAccruals, SanergyCalendar, Leave_Entitlement_Utilization)
from .serializers import Comment, CommentSerializer, LeaveRequestsSerializer


def leave_application(request):
    
    return render(request, 'users/login.html', )


# def individual_leave_history(request, id=None):
#     current_user = request.user
#     if Employee.objects.filter(email=(current_user.email)).exists():
#         user_history = EmployeeLeaveRequest.objects.filter(employee = (current_user.salesforceid)).order_by('-Id')[:5][::-1]
#         context={
#             'user_history':user_history,
#             'current_user': current_user,
#             }

#         #  WHO IS OUT-GET USER INSTANCE, AND DEPARTMENT UNIT
#         user_sfid = current_user.salesforceid
#         employee = Employee.objects.get(Id=user_sfid)
#         employee_department_unit_id = employee.Sanergy_Department_Unit

#         # THE, GRAB LEAVES THAT SHARE THE DEPARTMENT UNIT WITH THE CURRENT USER
#         # LEAVES TO SHOW, SAME DEPARTMENT, APPROVED BY HR, NOT OVER NY END DAY TODAY
        
#         hr_approved_leaves =  EmployeeLeaveRequest.objects.filter(
#             employee_s_department = employee_department_unit_id,
#             approval_status = "Approved by HR",
#             leave_end_date__lt = datetime.date.today())
#         pending_approval_leaves =  EmployeeLeaveRequest.objects.filter(
#             employee_s_department = employee_department_unit_id,
#             approval_status = "Pending Approval",
#             leave_end_date__lt = datetime.date.today())

#         colleagues_leaves = hr_approved_leaves | pending_approval_leaves
#         # for leaves in colleagues_leaves:
#             # print(leaves.employee)
#             # print(leaves.approval_status)
#             # print(leaves.leave_start_date)
#             # print(leaves.leave_end_date)

#             # print(colleagues_leaves.count())

#         context['colleagues_leaves'] = colleagues_leaves
#         return context



        # fetching leave types 
def leave_entitlement_types(request):
    sf = salesforcelogin()
    leave_type_data = sf.bulk.Leave_Entitlement_Type_Config__c.query(
         "SELECT Id,name,Leave_Type__c, Leave_Group__c from Leave_Entitlement_Type_Config__c where Year__c = 2018")
    context = {
        'leave_type_data': leave_type_data
    }
    for leave_types in leave_type_data:
        # # saving every leave type in postgress
        Leave_Entitlement_Type.objects.update_or_create(Id=leave_types['Id'],
                                 Name=leave_types["Name"],
                                 Leave_Type=leave_types["Leave_Type__c"],
                                 Leave_Group=leave_types["Leave_Group__c"])

    
    leaveTypes=Leave_Entitlement_Type.objects.all()

    return HttpResponse(leaveTypes)
   


def populate_leaveAccruals(request):
    sf = salesforcelogin()
    data = sf.bulk.Leave_Accrual__c.query(
        "SELECT Days_Accrued__c,"
        "Days_Worked__c,"
        "Employee__c,"
        "Leave_Entitlement_Utilization__c,"
        "Period__c from Leave_Accrual__c")
    context = {
        'data': data
    }

    for accrual  in data:
        days_accrued = accrual["Days_Accrued__c"]
        days_worked = accrual["Days_Worked__c"]
        employee = accrual["Employee__c"]
        leave_entitlement_utilization = accrual["Leave_Entitlement_Utilization__c"]
        period = accrual["Period__c"]

        # map these accruals to database
        LeaveAccruals.objects.update_or_create(
                                               Days_Accrued= days_accrued,
                                               Days_Worked = days_worked,
                                               Employee = employee,
                                               Leave_Entitlement_Utilization = leave_entitlement_utilization,
                                               Period = period)

    #Continue from this point:
    accruals = LeaveAccruals.objects.all()
    for item in accruals:
        context['accruals'] = accruals
    return render(request, 'leave_management/accruals.html', context)


def populate_employee_leave_request(request):
    sf = salesforcelogin()
    data = sf.bulk.Employee_Leave_Request__c.query(
        "SELECT Id,"
        "Approval_Status__c,"
        "Comments__c,"
        "Coverage_Plans__c,"
        "Department_Team_lead__c,"
        "Employee__c,"
        "Employee_s_Department__c,"
        "HR_Approve_Cancellation__c,"
        "Leave_Approved__c,"
        "Leave_End_Date__c,"
        "Leave_Entitlement_Utilization__c,"
        "Leave_Start_Date__c,"
        "Leave_Started__c,"
        "Leave_Type__c,"
        "Line_Manager_Account__c,"
        "Line_Manager_Approve_Cancellation__c,"
        "Next_Step__c, Next_Step_Due_Date__c,"
        "No_Of_Approved_Leave_Days__c,"
        "No_Of_Leave_Days_Requested__c,"
        "Request_From_VFP__c,"
        "Sick_Leave_Doc_Attached__c, Stage__c, StartEndDate__c  from Employee_Leave_Request__c ORDER BY CreatedDate DESC")

    context = {
        'data': data
    }

    for leave_request  in data:
        Id = leave_request['Id']
        Approval_status = leave_request["Approval_Status__c"]
        Comments = leave_request["Comments__c"]
        Coverage_Plans = leave_request["Coverage_Plans__c"]
        Department_Team_lead = leave_request["Department_Team_Lead__c"]
        employee = leave_request["Employee__c"]
        Employee_s_Department = leave_request["Employee_s_Department__c"]
        HR_Approve_Cancellation = leave_request["HR_Approve_Cancellation__c"]
        Leave_Approved  = leave_request["Leave_Approved__c"]
        Leave_End_Date  = leave_request["Leave_End_Date__c"]
        Leave_Entitlement_Utilization = leave_request["Leave_Entitlement_Utilization__c"]
        Leave_Start_Date  = leave_request["Leave_Start_Date__c"]
        Leave_Started = leave_request["Leave_Started__c"]
        Leave_Type = leave_request["Leave_Type__c"]
        Line_Manager_Account = leave_request["Line_Manager_Account__c"]
        Line_Manager_Approve_Cancellation = leave_request["Line_Manager_Approve_Cancellation__c"]
        Next_Step  = leave_request["Next_Step__c"]
        Next_Step_Due_Date = leave_request["Next_Step_Due_Date__c"]
        No_Of_Approved_Leave_Days = leave_request["No_Of_Approved_Leave_Days__c"]
        No_Of_Leave_Days_Requested = leave_request["No_Of_Leave_Days_Requested__c"]
        Request_From_VFP  = leave_request["Request_From_VFP__c"]
        Sick_Leave_Doc_Attached = leave_request["Sick_Leave_Doc_Attached__c"]
        Stage  = leave_request["Stage__c"]
        StartEndDate  = leave_request["StartEndDate__c"]

        # CREATING EMPLOYEE INSTANCE AND SAVING
        employee = Employee.objects.get(Id = employee)

        # map these accruals to database
        EmployeeLeaveRequest.objects.update_or_create(Id=Id,
                                        defaults={
                                        "approval_status":  Approval_status,
                                        "comments":  Comments,
                                        "coverage_plans": Coverage_Plans,
                                        "department_team_lead": Department_Team_lead,
                                        "employee": employee,
                                        "employee_s_department": Employee_s_Department,
                                        "HR_approve_cancellation": HR_Approve_Cancellation,
                                        "leave_approved": Leave_Approved,
                                        "leave_end_date": Leave_End_Date,
                                        "leave_entitlement_utilization":  Leave_Entitlement_Utilization,
                                        "leave_start_date": Leave_Start_Date,
                                        "leave_started": Leave_Started,
                                        "leave_type": Leave_Type,
                                        "line_manager_account": Line_Manager_Account,
                                        "line_manager_approve_cancellation": Line_Manager_Approve_Cancellation,
                                        "next_step": Next_Step,
                                        "next_step_due_date": Next_Step_Due_Date,
                                        "no_of_approved_leave_days": No_Of_Approved_Leave_Days,
                                        "no_of_leave_days_requested": No_Of_Leave_Days_Requested,
                                        "request_from_VFP": Request_From_VFP,
                                        "sick_leave_doc_attached": Sick_Leave_Doc_Attached,
                                        "stage": Stage,
                                        "startEndDate": StartEndDate
                                        } )

    #Continue from this point:
    requests = EmployeeLeaveRequest.objects.all()
    for item in requests:
        context['requests'] = requests
    return HttpResponse('Done Shipping Leaves to Postgres')


def populate_sanergy_calender(request):
    sf = salesforcelogin()
    data = sf.bulk.Sanergy_Calendar__c.query(
        "SELECT Date__c,"
        "Description__c,"
        "isBusinessDay__c,"
        "isBusinessDayInclSat__c,"
        "IsHoliday__c,"
        "IsWeekend__c,"
        "is_Weekend_or_Holiday__c,"
        "Weekday_Name__c,"
        "Weekday_No__c from Sanergy_Calendar__c")

    context = {
        'data': data
    }

    for item in data:
        Date__c = item['Date__c']
        Description__c = item['Description__c']
        isBusinessDay__c = item['isBusinessDay__c']
        isBusinessDayInclSat__c = item['isBusinessDayInclSat__c']
        IsHoliday__c = item['IsHoliday__c']
        IsWeekend__c = item['IsWeekend__c']
        is_Weekend_or_Holiday__c = item['is_Weekend_or_Holiday__c']
        Weekday_Name__c = item['Weekday_Name__c']
        Weekday_No__c = item['Weekday_No__c']

        # sending to database
        SanergyCalendar.objects.update_or_create(Date=Date__c,
                                defaults={
                                'Decsritption' : Description__c,
                                'isBusinessDay' : isBusinessDay__c,
                                'isBusinessDayInclSat' : isBusinessDayInclSat__c,
                                'isHoliday' : IsHoliday__c,
                                'isWeekend' : IsWeekend__c,
                                'isWeekend_or_Holiday' : is_Weekend_or_Holiday__c,
                                'Weekday_Name' : Weekday_Name__c,
                                'Weekday_No' : Weekday_No__c,
                                })

    calendar = SanergyCalendar.objects.all()
    for kitu in calendar:
        print(kitu.Weekday_Name)
    messages.add_message (request, messages.INFO, 'Calendar is Ready!')
    return JsonResponse(data, safe=False)

# Populate leave entitlement utilization 
def entitlement_utilization(request):
    sf = salesforcelogin()

    data = sf.bulk.Leave_Entitlement_Utilization__c.query(
        "SELECT id,"
        "Accrued_To_Date_Selected__c,"
        "Employee__c,"
        "Leave_Days_Accrued__c,"
        "Leave_Days_Remaining__c,"
        "Leave_Days_Scheduled__c,"
        "Leave_Days_Used__c,"
        "Leave_Entitlement_Type_Config__c,"
        "Leave_Type__c,"
        "Leave_Type_Name__c,"
        "Leave_Year__c,"
        "Total_No_of_Leave_Days__c from Leave_Entitlement_Utilization__c ")
  
    context = {
        'data': data
    }
    print(context['data'])

    for item in data:
        id = item['Id']
        Accrued_To_Date_Selected = item['Accrued_To_Date_Selected__c']
        Employee = item['Employee__c']
        Leave_Days_Accrued = item['Leave_Days_Accrued__c']
        Leave_Days_Remaining = item['Leave_Days_Remaining__c']
        Leave_Days_Scheduled = item['Leave_Days_Scheduled__c']
        Leave_Days_Used = item['Leave_Days_Used__c']
        Leave_Entitlement_Type_Config = item['Leave_Entitlement_Type_Config__c']
        Leave_Type = item['Leave_Type__c']
        Leave_Type_Name = item['Leave_Type_Name__c']
        Leave_Year  = item['Leave_Year__c']
        Total_No_of_Leave_Days = item['Total_No_of_Leave_Days__c']

        Leave_Entitlement_Utilization.objects.update_or_create(
                                    id = id ,
                                    defaults={
                                    "Accrued_To_Date_Selected" : Accrued_To_Date_Selected,
                                    "Employee" : Employee,
                                    "Leave_Days_Accrued" : Leave_Days_Accrued,
                                    "Leave_Days_Remaining" : Leave_Days_Remaining,
                                    "Leave_Days_Scheduled" : Leave_Days_Scheduled,
                                    "Leave_Days_Used" : Leave_Days_Used,
                                    "Leave_Entitlement_Type_Config" : Leave_Entitlement_Type_Config,
                                    "Leave_Type" : Leave_Type,
                                    "Leave_Type_Name" : Leave_Type_Name,
                                    "Leave_Year" : Leave_Year,
                                    "Total_No_of_Leave_Days" : Total_No_of_Leave_Days,
                                    })

    
    return JsonResponse(data, safe=False)




# Refresh sanergy Calendar
def refresh_sanergy_calender(request):
    sf = salesforcelogin()
    data = sf.bulk.Sanergy_Calendar__c.query(
        "SELECT Date__c,"
        "Description__c,"
        "isBusinessDay__c,"
        "isBusinessDayInclSat__c,"
        "IsHoliday__c,"
        "IsWeekend__c,"
        "is_Weekend_or_Holiday__c,"
        "Weekday_Name__c,"
        "Weekday_No__c from Sanergy_Calendar__c WHERE CreatedDate = TODAY OR LastModifiedDate = TODAY")

    context = {
        'data': data
    }

    for item in data:
        Date__c = item['Date__c']
        Description__c = item['Description__c']
        isBusinessDay__c = item['isBusinessDay__c']
        isBusinessDayInclSat__c = item['isBusinessDayInclSat__c']
        IsHoliday__c = item['IsHoliday__c']
        IsWeekend__c = item['IsWeekend__c']
        is_Weekend_or_Holiday__c = item['is_Weekend_or_Holiday__c']
        Weekday_Name__c = item['Weekday_Name__c']
        Weekday_No__c = item['Weekday_No__c']

        # sending to database
        SanergyCalendar.objects.update_or_create(Date=Date__c,
                                defaults={
                                'Decsritption' : Description__c,
                                'isBusinessDay' : isBusinessDay__c,
                                'isBusinessDayInclSat' : isBusinessDayInclSat__c,
                                'isHoliday' : IsHoliday__c,
                                'isWeekend' : IsWeekend__c,
                                'isWeekend_or_Holiday' : is_Weekend_or_Holiday__c,
                                'Weekday_Name' : Weekday_Name__c,
                                'Weekday_No' : Weekday_No__c,
                                })
        return HttpResponse("the calendar is populated")



def leaves(request):
    user = user = request.user.salesforceid
    connection = postgressConnection()
    year = '2020.0'
    cursor = connection.cursor()
    strleave_type = "SELECT \"Leave_Type\", \"id\"  FROM  leave_management_leave_entitlement_utilization  WHERE \"Leave_Year\"='"+ year +"' AND \"Employee\"='"+ user +"'"
    cursor.execute(strleave_type)
    leave = cursor.fetchall()
    return leave


def request_leave(request):
    user = request.user.salesforceid 
    leave = leaves(request) 
    # history = individual_leave_history(request)

    # leave balances code
    sf = salesforcelogin()
    
    leave_balance_object = sf.bulk.Leave_Entitlement_Utilization__c.query(
        "SELECT Leave_Type__c,"
        "Leave_Days_Remaining__c FROM  Leave_Entitlement_Utilization__c WHERE Employee__c='"+ user +"' AND Leave_Year__c =2020")


    context = {
        'leave': leave,
        # 'history': history,
        # 'user_history':history['user_history'],
        # 'colleagues_leaves':history['colleagues_leaves'],
        'anual_leave': leave_balance_object[0]['Leave_Type__c'],
        'anual_leave_remaining': leave_balance_object[0]['Leave_Days_Remaining__c'],
        'exam_leave': leave_balance_object[1]['Leave_Type__c'],
        'exam_leave_remaining': leave_balance_object[1]['Leave_Days_Remaining__c'],
        'compassionate_leave': leave_balance_object[2]['Leave_Type__c'],
        'compassionate_leave_remaining': leave_balance_object[2]['Leave_Days_Remaining__c']
        
    }
    
    return render(request, 'registration/request.html', context)


def request_leave_data(request):
        user = request.user.salesforceid
        context={}
    
        if request.method == 'POST':
            start_date = request.POST['startdate']
            start_date1 = pd.to_datetime(start_date,format="%Y/%m/%d").date()
            end_date = request.POST['enddate']
            end_date1 = pd.to_datetime(end_date,format="%Y/%m/%d").date()
            total_selected_days = np.busday_count( start_date1 , end_date1)
        
            comments = request.POST['comments']
            coverage = request.POST['coverage'] 
            
            connection = postgressConnection()
            cursor= connection.cursor()
            days_selected = "SELECT \"Date\",\"Weekday_Name\", \"Decsritption\", \"isWeekend\" ,CASE WHEN \"isWeekend_or_Holiday\" = FALSE THEN 0 ELSE 1 END AS \"CountAsLeave\" FROM leave_management_sanergycalendar WHERE \"Date\" BETWEEN '" + start_date + "' AND '" + end_date + "' ORDER BY \"Date\" ASC"
            cursor.execute(days_selected)
            days_requested = cursor.fetchall()
        
         
        leave = leaves(request) 
           
            
        leave_type_selected= request.POST.getlist('leave_name')
        leave_type_selected = leave_type_selected[0]
                    
        def leave_desplayed():
            for i in leave:
                if i[1] == leave_type_selected:
                    return i[0]
        
        leave_to_display = leave_desplayed()
        # history = individual_leave_history(request)

        # leave balances code
        sf = salesforcelogin()
        leave_balance_object = sf.bulk.Leave_Entitlement_Utilization__c.query(
            "SELECT Leave_Type__c,"
            "Leave_Days_Remaining__c FROM  Leave_Entitlement_Utilization__c WHERE Employee__c='"+ user +"' AND Leave_Year__c =2020")


        
        context = {
            'days': days_requested,
            'leave': leave,
            'comments': comments,
            'leave_type_selected': leave_type_selected,
            'Leave_display': leave_to_display,
            'coverage': coverage,
            # 'user_history':history['user_history'],
            # 'colleagues_leaves':history['colleagues_leaves'],
            'anual_leave': leave_balance_object[0]['Leave_Type__c'],
            'anual_leave_remaining': leave_balance_object[0]['Leave_Days_Remaining__c'],
            'exam_leave': leave_balance_object[1]['Leave_Type__c'],
            'exam_leave_remaining': leave_balance_object[1]['Leave_Days_Remaining__c'],
            'compassionate_leave': leave_balance_object[2]['Leave_Type__c'],
            'compassionate_leave_remaining': leave_balance_object[2]['Leave_Days_Remaining__c'],
            'days_selected': total_selected_days + 1
        }
        
        
        
        return render(request, 'registration/request.html', context)


# @api_view(('GET',))
def post_leave_to_salesforce(request):
    user = request.user.salesforceid
    start_date = request.POST.getlist('date')[0]
    end_date = request.POST.getlist('date')[-1]
    days_selected = request.POST.getlist('half_day')
    days_requested = sum(map(float,days_selected))
    leave_submitted = request.POST['leave_type']
    
    coverage = request.POST.getlist('coverage')[0]
    comments = request.POST.getlist('comments')[0]

    
    leave = leaves(request)
    # history = individual_leave_history(request)

    department_object= Employee.objects.get(Id=user)
    
    sf = salesforcelogin()
    leave_balance_object = sf.bulk.Leave_Entitlement_Utilization__c.query(
        "SELECT Leave_Type__c,"
        "Leave_Days_Remaining__c FROM  Leave_Entitlement_Utilization__c WHERE Employee__c='"+ user +"' AND Leave_Year__c =2020")
    
    def comments_switch():
        leave_balance_object = sf.bulk.Leave_Entitlement_Utilization__c.query(
        "SELECT Leave_Days_Remaining__c FROM  Leave_Entitlement_Utilization__c WHERE Employee__c='"+ user +"' AND id='"+ leave_submitted +"' AND Leave_Year__c =2020")
        leave_balance_object= leave_balance_object[0]['Leave_Days_Remaining__c']

        if days_requested > leave_balance_object:
            return comments + ". NOTE: The leave requested surpuses the days accrued"
        else:
            return comments

    comment_submit = comments_switch()
        
    context = {
        'leave': leave,
        # 'user_history':history['user_history'],
        # 'colleagues_leaves':history['colleagues_leaves'],
        'department_unit': department_object.Sanergy_Department_Unit,
        'anual_leave': leave_balance_object[0]['Leave_Type__c'],
        'anual_leave_remaining': leave_balance_object[0]['Leave_Days_Remaining__c'],
        'exam_leave': leave_balance_object[1]['Leave_Type__c'],
        'exam_leave_remaining': leave_balance_object[1]['Leave_Days_Remaining__c'],
        'compassionate_leave': leave_balance_object[2]['Leave_Type__c'],
        'compassionate_leave_remaining': leave_balance_object[2]['Leave_Days_Remaining__c'],
        'days_requested': days_requested
    }

    department = context['department_unit']


    sf = salesforcelogin()
    start_and_end_year = sf.bulk.Leave_Entitlement_Type_Config__c.query(
        "SELECT Year_End_Date__c, Year_Start_Date__c from Leave_Entitlement_Type_Config__c WHERE Year__c= 2020")
    org_start_year= start_and_end_year[0]['Year_Start_Date__c']
    org_end_year = start_and_end_year[0]['Year_End_Date__c']

    # Date convertions 
    org_start_year = datetime.strptime(org_start_year, "%Y-%m-%d")
    org_start_year_time_stamp= datetime.timestamp(org_start_year)
    
    org_end_year = datetime.strptime(org_end_year, "%Y-%m-%d")
    org_end_year_time_stamp= datetime.timestamp(org_end_year)
    
    user_start_date = datetime.strptime(start_date, "%Y-%m-%d")
    user_start_date_time_stamp= datetime.timestamp(user_start_date)
    

    user_end_date = datetime.strptime(end_date, "%Y-%m-%d")
    user_end_date_time_stamp= datetime.timestamp(user_end_date)
    
    

    data = {
        "Employee_s_Department__c" :department, 
        "Request_From_VFP__c":True, 
        "Employee__c": user, 
        "Leave_End_Date__c": end_date, 
        "No_Of_Leave_Days_Requested__c": days_requested, 
        "Leave_Entitlement_Utilization__c": leave_submitted, 
        "Leave_Start_Date__c": start_date, 
        "Coverage_Plans__c": coverage, 
        "Comments__c": comment_submit
        }
    if user_start_date_time_stamp >= org_start_year_time_stamp:
        query = sf.Employee_Leave_Request__c.create(data)
        messages.info(request, "Your leave request has been submitted successfuly!")

    else:
        print("not submitting")
        messages.error(request,  "Your have selected incorrect date ranges!")


    return render(request, 'registration/request.html', context)


    