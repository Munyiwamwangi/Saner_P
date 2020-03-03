import hashlib
import uuid

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Email imports:
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from employee.models import Employee

from .models import CustomUser
from .passwordgenerator import generatePassword
from .utils import postgressConnection

salt = uuid.uuid4().hex




# Create your views here.

def home(request):
    return render(request, 'registration/login.html')

def password_reset(request):
    return render(request, 'users/password_reset_form.html')

def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html')

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')

def create_custom_user(request):
    employee = Employee.objects.filter(email__isnull=False).exclude(Id__isnull=True)
    context={ }
    
    for field in employee:
        email = field.email
        salesforceid = field.Id
        password = generatePassword(10)
        print(password)
        print(email)


        password = make_password(password, None, 'default')
        # print(password)

        #METHOD2 :  hashing the password with salt, store as raw bytes
        # password2 = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        # print(password2)
        
        first_name = field.Employee_First_Name
        full_name = field.Employee_Full_Name

        # CustomUser.objects.update_or_create(salesforceid = salesforceid,
        #                         defaults={
        #                             'email':email,
        #                             'password':password,
        #                             'first_name':first_name,
        #                             })


        employee = CustomUser.objects.all()
        context['employee'] = employee
        print(employee.count())
        
    return render(request, 'employee/employee_directory.html', context)


@login_required
def user_directory(request):
    current_user = request.user
    employee = CustomUser.objects.all()
    context = {}
    context['employee'] = employee
    print(employee.count())
    return render(request, 'employee/employee_directoryhtml.html', context)
