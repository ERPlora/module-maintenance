"""Tests for maintenance models."""
import pytest
from django.utils import timezone

from maintenance.models import MaintenanceOrder


@pytest.mark.django_db
class TestMaintenanceOrder:
    """MaintenanceOrder model tests."""

    def test_create(self, maintenance_order):
        """Test MaintenanceOrder creation."""
        assert maintenance_order.pk is not None
        assert maintenance_order.is_deleted is False

    def test_str(self, maintenance_order):
        """Test string representation."""
        assert str(maintenance_order) is not None
        assert len(str(maintenance_order)) > 0

    def test_soft_delete(self, maintenance_order):
        """Test soft delete."""
        pk = maintenance_order.pk
        maintenance_order.is_deleted = True
        maintenance_order.deleted_at = timezone.now()
        maintenance_order.save()
        assert not MaintenanceOrder.objects.filter(pk=pk).exists()
        assert MaintenanceOrder.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, maintenance_order):
        """Test default queryset excludes deleted."""
        maintenance_order.is_deleted = True
        maintenance_order.deleted_at = timezone.now()
        maintenance_order.save()
        assert MaintenanceOrder.objects.filter(hub_id=hub_id).count() == 0


