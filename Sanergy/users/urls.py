from django.urls import path
from . import views
# from ..leave_management.views import request_leave
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('reset/done/', views.password_reset_done, name='password_reset_done'),
    path('create_custom_user/', views.create_custom_user, name='create_custom_user'),
    path('user_directory/', views.user_directory, name='user_directory'),
    # path('leave_page', views.request_leave, name='leave_page'),
]
