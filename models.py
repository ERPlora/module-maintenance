from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

MAINT_TYPE = [
    ('preventive', _('Preventive')),
    ('corrective', _('Corrective')),
    ('predictive', _('Predictive')),
]

class MaintenanceOrder(HubBaseModel):
    reference = models.CharField(max_length=50, verbose_name=_('Reference'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    maintenance_type = models.CharField(max_length=20, default='corrective', choices=MAINT_TYPE, verbose_name=_('Maintenance Type'))
    priority = models.CharField(max_length=20, default='medium', verbose_name=_('Priority'))
    status = models.CharField(max_length=20, default='pending', verbose_name=_('Status'))
    scheduled_date = models.DateField(null=True, blank=True, verbose_name=_('Scheduled Date'))
    completed_date = models.DateField(null=True, blank=True, verbose_name=_('Completed Date'))
    assigned_to = models.UUIDField(null=True, blank=True, verbose_name=_('Assigned To'))
    cost = models.DecimalField(max_digits=10, decimal_places=2, default='0', verbose_name=_('Cost'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'maintenance_maintenanceorder'

    def __str__(self):
        return self.title

