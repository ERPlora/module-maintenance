from django import forms
from django.utils.translation import gettext_lazy as _

from .models import MaintenanceOrder

class MaintenanceOrderForm(forms.ModelForm):
    class Meta:
        model = MaintenanceOrder
        fields = ['reference', 'title', 'description', 'maintenance_type', 'priority', 'status', 'scheduled_date', 'completed_date', 'assigned_to', 'cost', 'notes']
        widgets = {
            'reference': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'title': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
            'maintenance_type': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'priority': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'status': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'scheduled_date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'completed_date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'assigned_to': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'cost': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'notes': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
        }

