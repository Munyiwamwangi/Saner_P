from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from PIL import Image


# Create your models here.
class CustomUserManager(BaseUserManager):
    '''
    Custom user model where the email is the unique identifier for authentication instead of usernames
    '''
    def create_user(self, email, password, **extra_fields):
        '''
        create and save a user with the given email and password
        '''
        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''
        Create and save a superuser with the given email and password
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class Employee(AbstractUser):
    username = None
    Id = models.CharField(primary_key=True,max_length=100, blank=False )
    Employee_First_Name = models.CharField(max_length=100, blank=False, null=True)
    Employee_Last_Name = models.CharField(max_length=100, null=True)
    Employee_Full_Name = models.CharField(max_length=100, blank=False)
    Company_Division = models.CharField(max_length=100, blank=True)
    Employee_Department = models.CharField(max_length=100, blank=True, null=True)
    Sanergy_Department = models.CharField(max_length=100, null=True)
    Sanergy_Department_Unit = models.CharField(max_length=100, null=True)
    Talent_Partner = models.CharField(max_length=100, null = True, blank=True)
    Team_Lead = models.CharField(max_length=100, blank=True, null=True )
    Employee_Active = models.BooleanField(default=True, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=100, null=True)
    HR_Employee_ID = models.EmailField(unique=True, null=True)
    Line_Manager = models.CharField(max_length=100, blank=False, null=True )
    IsDeleted = models.BooleanField(null=True)
    Image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Date_Of_Birth = models.DateField(default=timezone.now)
    Joined_Date = models.DateField(default=timezone.now)
    Phone_Number = models.CharField(max_length=15, blank=True, null=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_employee = models.BooleanField(default=True, null=True)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.Employee_Full_Name
