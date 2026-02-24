"""Tests for maintenance views."""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestDashboard:
    """Dashboard view tests."""

    def test_dashboard_loads(self, auth_client):
        """Test dashboard page loads."""
        url = reverse('maintenance:dashboard')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_dashboard_htmx(self, auth_client):
        """Test dashboard HTMX partial."""
        url = reverse('maintenance:dashboard')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_dashboard_requires_auth(self, client):
        """Test dashboard requires authentication."""
        url = reverse('maintenance:dashboard')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestMaintenanceOrderViews:
    """MaintenanceOrder view tests."""

    def test_list_loads(self, auth_client):
        """Test list view loads."""
        url = reverse('maintenance:maintenance_orders_list')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_list_htmx(self, auth_client):
        """Test list HTMX partial."""
        url = reverse('maintenance:maintenance_orders_list')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_list_search(self, auth_client):
        """Test list search."""
        url = reverse('maintenance:maintenance_orders_list')
        response = auth_client.get(url, {'q': 'test'})
        assert response.status_code == 200

    def test_list_sort(self, auth_client):
        """Test list sorting."""
        url = reverse('maintenance:maintenance_orders_list')
        response = auth_client.get(url, {'sort': 'created_at', 'dir': 'desc'})
        assert response.status_code == 200

    def test_export_csv(self, auth_client):
        """Test CSV export."""
        url = reverse('maintenance:maintenance_orders_list')
        response = auth_client.get(url, {'export': 'csv'})
        assert response.status_code == 200
        assert 'text/csv' in response['Content-Type']

    def test_export_excel(self, auth_client):
        """Test Excel export."""
        url = reverse('maintenance:maintenance_orders_list')
        response = auth_client.get(url, {'export': 'excel'})
        assert response.status_code == 200

    def test_add_form_loads(self, auth_client):
        """Test add form loads."""
        url = reverse('maintenance:maintenance_order_add')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_add_post(self, auth_client):
        """Test creating via POST."""
        url = reverse('maintenance:maintenance_order_add')
        data = {
            'reference': 'New Reference',
            'title': 'New Title',
            'description': 'Test description',
            'maintenance_type': 'New Maintenance Type',
            'priority': 'New Priority',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_edit_form_loads(self, auth_client, maintenance_order):
        """Test edit form loads."""
        url = reverse('maintenance:maintenance_order_edit', args=[maintenance_order.pk])
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_edit_post(self, auth_client, maintenance_order):
        """Test editing via POST."""
        url = reverse('maintenance:maintenance_order_edit', args=[maintenance_order.pk])
        data = {
            'reference': 'Updated Reference',
            'title': 'Updated Title',
            'description': 'Test description',
            'maintenance_type': 'Updated Maintenance Type',
            'priority': 'Updated Priority',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_delete(self, auth_client, maintenance_order):
        """Test soft delete via POST."""
        url = reverse('maintenance:maintenance_order_delete', args=[maintenance_order.pk])
        response = auth_client.post(url)
        assert response.status_code == 200
        maintenance_order.refresh_from_db()
        assert maintenance_order.is_deleted is True

    def test_bulk_delete(self, auth_client, maintenance_order):
        """Test bulk delete."""
        url = reverse('maintenance:maintenance_orders_bulk_action')
        response = auth_client.post(url, {'ids': str(maintenance_order.pk), 'action': 'delete'})
        assert response.status_code == 200
        maintenance_order.refresh_from_db()
        assert maintenance_order.is_deleted is True

    def test_list_requires_auth(self, client):
        """Test list requires authentication."""
        url = reverse('maintenance:maintenance_orders_list')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestSettings:
    """Settings view tests."""

    def test_settings_loads(self, auth_client):
        """Test settings page loads."""
        url = reverse('maintenance:settings')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_settings_requires_auth(self, client):
        """Test settings requires authentication."""
        url = reverse('maintenance:settings')
        response = client.get(url)
        assert response.status_code == 302

