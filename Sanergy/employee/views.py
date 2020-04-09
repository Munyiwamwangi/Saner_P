from django.contrib import messages
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import get_object_or_404, redirect, render

from leave_management.models import SanergyDepartment, SanergyDepartmentUnit
from leave_management.views import salesforcelogin
from users.models import CustomUser

from .filters import EmployeeFilter
from .models import Employee


def landing(request):
    context = { 'current_user':request.user,}
    return render (request, 'users/landing.html', context)


def search(request):
    context={'departments' : SanergyDepartment.objects.all().order_by('name') }
    context['team_lead'] = Employee.objects.filter(team_lead__isnull=False).distinct()
    context['department_unit'] = SanergyDepartmentUnit.objects.all().order_by('name')
    context['current_user_profile'] = Employee.objects.filter(Id = request.user.salesforceid).first()
    context['employee'] = Employee.objects.all()
    return render(request, 'employee/search_list.html', context)


# @login_required
def employee_directory(request):
    context = { 'employee':Employee.objects.filter(Employee_Active = True).order_by('email') }
    return render(request, 'employee/employee_list.html', context)


# @login_required
def user_directory(request):
    context = { 'employee' : CustomUser.objects.all() }
    return render(request, 'employee/employee_directoryhtml.html', context)


# PERSONAL PROFILE
def employee_profile(request, Id):
    current_user = request.user
    if Employee.objects.filter(Id = request.user.salesforceid).exists():
        context={'current_user_profile' : Employee.objects.filter(Id = request.user.salesforceid).first()}
        context ['employee'] = Employee.objects.get(Id  = Id)
    else:
        messages.warning(request, 'You must be an employee to view someone\'s profile through this platform', extra_tags='alert')
        return redirect('employee_directory')
    return render(request, 'employee/profile.html', context)


# POPULATING Employee details SOQL
# @login_required
def populate_postgres(request):
    sf = salesforcelogin()
    employee_list = []
    data = sf.bulk.Employee__c.query(
        "SELECT Id, Employee_Role__c, Primary_Phone__c, Leave_Group__c, Employee_SF_Account__c, Employee_Last_Name__c,"
        "HR_Employee_ID__c, Employee_Active__c, Employee_First_Name__c, name, Work_Email__c, Department__c, Employee_Middle_Name__c,"
        "Sanergy_Department__c, Sanergy_Department_Unit__c, Talent_Partner__c, Team_Lead__c,  Line_Manager__c, IsDeleted from Employee__c ")

    context = {
        'data': data
    }
    # return JsonResponse(data, safe=False)

    for employee_data in data:        
        Employee.objects.update_or_create(Id=employee_data["Id"],
                                    defaults={
                                    'Employee_Full_Name' : employee_data["Name"],
                                    'Primary_Phone' : employee_data['Primary_Phone__c'],
                                    'Employee_Role' : employee_data['Employee_Role__c'],
                                    'Leave_Group' : employee_data['Leave_Group__c'],
                                    'email' : employee_data["Work_Email__c"],
                                    'HR_Employee_ID': employee_data["HR_Employee_ID__c"],
                                    'Employee_Active':  employee_data["Employee_Active__c"],
                                    'Employee_First_Name': employee_data["Employee_First_Name__c"],
                                    'Employee_Middle_Name': employee_data['Employee_Middle_Name__c'],
                                    'Employee_Last_Name' : employee_data['Employee_Last_Name__c'],
                                    'IsDeleted' : employee_data["IsDeleted"],
                                    'Sanergy_Department' : employee_data['Sanergy_Department__c'],
                                    'Sanergy_Department_Unit' : employee_data['Sanergy_Department_Unit__c'],
                                    })

    '''
    UPDATE REFERENTIAL  KEYS Line Manager, Talent Partner, Team Lead
    '''
    for employee_data in data:
            Id = employee_data["Id"]
            Line_Manager__c = employee_data['Line_Manager__c']
            Talent_Partner__c = employee_data['Talent_Partner__c']
            Team_Lead__c = employee_data['Team_Lead__c']

            try:
                Employee.objects.update_or_create(Id=Id,
                                        defaults={
                                        'Line_Manager': Employee.objects.get(Id=Line_Manager__c),
                                        'Team_Lead': Employee.objects.get(Id=Team_Lead__c),
                                        'Talent_Partner': Employee.objects.get(Id=Talent_Partner__c),
                                        })
            except Exception as e:
                if Line_Manager__c == None:
                    print(e , " Line manager not available for : ", employee_data["Name"])
                elif Team_Lead__c == None:
                    print(e , " Team Lead not available for : ", employee_data["Name"])
                elif Talent_Partner__c == None:
                    print(e , " Talent Partner not available for : ", employee_data["Name"])
                else:
                    print("Something went Wrong")
               

            employee = Employee.objects.all()
            
            for item in employee:
                context['employee'] = employee

    return render(request, 'employee/employee_directory.html', context)
    # return JsonResponse(data, safe=False)


# Refresh Employee details from SF to PGres
def refresh_employees():
    sf = salesforcelogin()
    data = sf.bulk.Employee__c.query(
        "SELECT Id,"
        "Line_Manager__c,"
        "HR_Employee_ID__c,"
        "Employee_Active__c,"
        "Employee_First_Name__c,"
        "name,Work_Email__c, Department__c,"
        "Sanergy_Department__c,"
        "Sanergy_Department_Unit__c,"
        "Talent_Partner__c,"
        "Team_Lead__c, "
        "IsDeleted from Employee__c WHERE CreatedDate = TODAY OR LastModifiedDate = TODAY")
        
    context = {
        'data': data
    }
    for employee_data in data:
        Id = employee_data["Id"]
        Line_Manager__c = employee_data["Line_Manager__c"]
        HR_Employee_ID__c = employee_data["HR_Employee_ID__c"]
        Employee_Active__c = employee_data["Employee_Active__c"]
        Employee_First_Name__c = employee_data["Employee_First_Name__c"]
        Name = employee_data["Name"]
        Work_Email__c = employee_data["Work_Email__c"]
        Department__c = employee_data["Department__c"]
        Sanergy_Department__c = employee_data['Sanergy_Department__c']
        Sanergy_Department_Unit__c = employee_data['Sanergy_Department_Unit__c']
        Talent_Partner__c = employee_data['Talent_Partner__c']
        Team_Lead__c = employee_data['Team_Lead__c']
        IsDeleted = employee_data["IsDeleted"]

        # Inserting them to database 
        Employee.objects.update_or_create(Id=Id,
                                    defaults={
                                    'Employee_Full_Name':Name,
                                    'Line_Manager':Line_Manager__c,
                                    'email':Work_Email__c,
                                    'HR_Employee_ID':HR_Employee_ID__c,
                                    'Employee_Active':Employee_Active__c,
                                    'Employee_First_Name':Employee_First_Name__c,
                                    'IsDeleted':IsDeleted,
                                    'Employee_Department':Department__c,
                                    'Sanergy_Department':Sanergy_Department__c,
                                    'Sanergy_Department_Unit':Sanergy_Department_Unit__c,
                                    'Talent_Partner':Talent_Partner__c,
                                    'Team_Lead':Team_Lead__c,
                                    })

    employee = Employee.objects.all()
    print(employee.count())
    for item in employee:
        context['employee'] = employee

    # print(context)
    # print('********************  list end ****************** list end **********************************************')

    # return render(request, 'employee/employee_directory.html', context)
    return JsonResponse(data, safe=False)

# schedule.every(1).day.do(refresh_employees)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
