from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('login', views.home, name='home'),
    path('', views.home, name='home'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('reset/', views.password_reset_confirm, name='password_reset_confirm'),


]
