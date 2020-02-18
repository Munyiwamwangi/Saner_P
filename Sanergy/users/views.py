from django.shortcuts import render
from django.contrib.auth.models import User
from .utils import postgressConnection
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


# Email imports:
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    return render(request, 'registration/login.html')

def password_reset(request):
    return render(request, 'users/password_reset_form.html')

def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html')

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')


