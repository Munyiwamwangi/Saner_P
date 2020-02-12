from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from users.utils import salesforcelogin

from .forms import LeaveApplicationForm
from .models import EmployeeLeaveRequest, Leave_Entitlement_Type, LeaveAccruals, SanergyCalendar


def leave_application(request):
    current_user = request.user
    print(current_user.email)
    context={}
    requested_days = 0
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = current_user
            leave.emp_id=current_user.id
            leave.save()
            
            messages.add_message (request, messages.INFO, 'leave application')
            return HttpResponse('leave application process in progress')

    else:
            
            form = LeaveApplicationForm()

    return render(request, 'leave_templates/leave_application.html', {"leaveform": form,})
    # return HttpResponse('Leave Application')

    requested_days = 0
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = current_user
            leave.emp_id=current_user.id
            leave.save()
            
            return redirect('leave_application')

        else:
            form = LeaveApplicationForm()

            leaves = Leave.print_all()
            return render(request, 'sanergytemplates/leave_application.html', {"lform": form, "leavess": leaves, 'requested_days': requested_days})

        # fetching leave types 
def leave_entitlement_types(request):
    sf = salesforcelogin()
    leave_type_data = sf.bulk.Leave_Entitlement_Type_Config__c.query(
         "SELECT Id,"
         "name,Leave_Type__c,"
         "Leave_Group__c from Leave_Entitlement_Type_Config__c where Year__c=2018")
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
    return HttpResponse('DB ostgreSQL updated Leave Types sucessfully !')
    # return JsonResponse(leave_types, safe=False)

  

def request_leave(request):
    sf = salesforcelogin()
    data = sf.Leave_Entitlement_Type_Config__c.create(
        {'Accrue__c': 'Start Month', 'Leave_Group__c': 'aJ87E0000004CAu', 'Leave_Type__c': 'Annual Leave', 'Total_No_of_Leave_Days__c': '5', 'Year__c': '2020'})
    return JsonResponse(data)


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



def employee_leave_request(request):
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
        "Sick_Leave_Doc_Attached__c,"
        "Stage__c, StartEndDate__c  from Employee_Leave_Request__c ")

    # print(type(data))
    # print(data)

    context = {
        'data': data
    }
    # return HttpResponse(data)


    for leave_request  in data:
        # Id = leave_request['Id']
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
        
        # map these accruals to local postgres db
        EmployeeLeaveRequest.objects.update_or_create(
                                            #    id = Id,
                                               approval_status= Approval_status,
                                               comments = Comments,
                                               coverage_plans= Coverage_Plans,
                                               department_team_lead = Department_Team_lead,
                                            #    employee = employee,
                                               employee_s_department= Employee_s_Department,
                                               HR_approve_cancellation = HR_Approve_Cancellation,
                                               leave_approved= Leave_Approved,
                                               leave_end_date = Leave_End_Date,
                                               leave_entitlement_utilization=  Leave_Entitlement_Utilization,
                                               leave_start_date= Leave_Start_Date,
                                               leave_started = Leave_Started,
                                               leave_type = Leave_Type,
                                               line_manager_account = Line_Manager_Account,
                                               line_manager_approve_cancellation = Line_Manager_Approve_Cancellation,
                                               next_step = Next_Step,
                                               next_step_due_date = Next_Step_Due_Date,
                                               no_of_approved_leave_days = No_Of_Approved_Leave_Days,
                                               no_of_leave_days_requested = No_Of_Leave_Days_Requested,
                                               request_from_VFP = Request_From_VFP,
                                            #    stage = Stage,
                                            #    startEndDate = StartEndDate
                                                )

    # Continue from this point:
    requests = EmployeeLeaveRequest.objects.all()
    for item in requests:
        context['requests'] = requests
    return render(request, 'leave_management/requests.html', context)


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