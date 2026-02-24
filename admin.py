from django.contrib import admin

from .models import MaintenanceOrder

@admin.register(MaintenanceOrder)
class MaintenanceOrderAdmin(admin.ModelAdmin):
    list_display = ['reference', 'title', 'maintenance_type', 'priority', 'created_at']
    search_fields = ['reference', 'title', 'description', 'maintenance_type']
    readonly_fields = ['created_at', 'updated_at']

