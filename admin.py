from django.contrib import admin

from .models import MaintenanceOrder

@admin.register(MaintenanceOrder)
class MaintenanceOrderAdmin(admin.ModelAdmin):
    list_display = ['reference', 'title', 'description', 'maintenance_type', 'priority']
    readonly_fields = ['id', 'hub_id', 'created_at', 'updated_at']
    ordering = ['-created_at']

