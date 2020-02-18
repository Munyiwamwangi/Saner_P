from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('reset/done/', views.password_reset_done, name='password_reset_done'),

]
