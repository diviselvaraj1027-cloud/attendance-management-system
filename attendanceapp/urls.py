from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_report, name='attendance_report'),
]