from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('work_orders/', views.work_orders, name='work_orders'),
    path('schedules/', views.schedules, name='schedules'),
    path('settings/', views.settings, name='settings'),
]
