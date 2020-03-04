from django.shortcuts import render
from django.contrib.auth.models import User
from .utils import postgressConnection
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404


from employee.models import Employee


# Email imports:
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model




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
    User = get_user_model()
    user = Employee.objects.filter(email__isnull=False).exclude(Id__isnull=True)
    context={
        'user':user
    }
    for field in user:
        email = field.email
        password = field.password
        Id = field.Id
        first_name = field.Employee_First_Name

        User.objects.update_or_create(Id=Id,
                                    defaults={
                                    'email' : email,
                                    'password' : password,
                                    'first_name': first_name})

    return HttpResponse("the users are populated")
