"""
Maintenance & CMMS Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('maintenance', 'dashboard')
@htmx_view('maintenance/pages/dashboard.html', 'maintenance/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('maintenance', 'work_orders')
@htmx_view('maintenance/pages/work_orders.html', 'maintenance/partials/work_orders_content.html')
def work_orders(request):
    """Work Orders view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('maintenance', 'schedules')
@htmx_view('maintenance/pages/schedules.html', 'maintenance/partials/schedules_content.html')
def schedules(request):
    """Schedules view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('maintenance', 'settings')
@htmx_view('maintenance/pages/settings.html', 'maintenance/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

