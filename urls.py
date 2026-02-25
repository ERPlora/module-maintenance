from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Navigation tab aliases
    path('work_orders/', views.maintenance_orders_list, name='work_orders'),
    path('schedules/', views.dashboard, name='schedules'),


    # MaintenanceOrder
    path('maintenance_orders/', views.maintenance_orders_list, name='maintenance_orders_list'),
    path('maintenance_orders/add/', views.maintenance_order_add, name='maintenance_order_add'),
    path('maintenance_orders/<uuid:pk>/edit/', views.maintenance_order_edit, name='maintenance_order_edit'),
    path('maintenance_orders/<uuid:pk>/delete/', views.maintenance_order_delete, name='maintenance_order_delete'),
    path('maintenance_orders/bulk/', views.maintenance_orders_bulk_action, name='maintenance_orders_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
