from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    salesforceid = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(unique=False, null=True)
    password = models.CharField(max_length=100, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ('email',)

    def __str__(self):
        return self.email