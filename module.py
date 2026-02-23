from django.utils.translation import gettext_lazy as _

MODULE_ID = 'maintenance'
MODULE_NAME = _('Maintenance & CMMS')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'build-outline'
MODULE_DESCRIPTION = _('Preventive and corrective maintenance for assets and equipment')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'operations'

MENU = {
    'label': _('Maintenance & CMMS'),
    'icon': 'build-outline',
    'order': 57,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Work Orders'), 'icon': 'build-outline', 'id': 'work_orders'},
{'label': _('Schedules'), 'icon': 'calendar-outline', 'id': 'schedules'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'maintenance.view_maintenanceorder',
'maintenance.add_maintenanceorder',
'maintenance.change_maintenanceorder',
'maintenance.delete_maintenanceorder',
'maintenance.manage_settings',
]
