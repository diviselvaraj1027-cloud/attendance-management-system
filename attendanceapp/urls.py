from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_report, name='attendance_report'),
    path('api/attendance/', views.api_attendance, name='api_attendance'),
]