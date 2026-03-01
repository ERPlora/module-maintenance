"""AI tools for the Maintenance module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListMaintenanceOrders(AssistantTool):
    name = "list_maintenance_orders"
    description = "List maintenance work orders."
    module_id = "maintenance"
    required_permission = "maintenance.view_maintenanceorder"
    parameters = {
        "type": "object",
        "properties": {
            "status": {"type": "string", "description": "pending, in_progress, completed, cancelled"},
            "maintenance_type": {"type": "string", "description": "preventive, corrective, predictive"},
            "priority": {"type": "string"}, "limit": {"type": "integer"},
        },
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from maintenance.models import MaintenanceOrder
        qs = MaintenanceOrder.objects.all()
        if args.get('status'):
            qs = qs.filter(status=args['status'])
        if args.get('maintenance_type'):
            qs = qs.filter(maintenance_type=args['maintenance_type'])
        if args.get('priority'):
            qs = qs.filter(priority=args['priority'])
        limit = args.get('limit', 20)
        return {"orders": [{"id": str(o.id), "reference": o.reference, "title": o.title, "maintenance_type": o.maintenance_type, "priority": o.priority, "status": o.status, "scheduled_date": str(o.scheduled_date) if o.scheduled_date else None, "cost": str(o.cost) if o.cost else None} for o in qs.order_by('-created_at')[:limit]]}


@register_tool
class CreateMaintenanceOrder(AssistantTool):
    name = "create_maintenance_order"
    description = "Create a maintenance work order."
    module_id = "maintenance"
    required_permission = "maintenance.add_maintenanceorder"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "title": {"type": "string"}, "description": {"type": "string"},
            "maintenance_type": {"type": "string", "description": "preventive, corrective, predictive"},
            "priority": {"type": "string"}, "scheduled_date": {"type": "string"},
            "assigned_to": {"type": "string"}, "cost": {"type": "string"},
            "notes": {"type": "string"},
        },
        "required": ["title", "maintenance_type"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from decimal import Decimal
        from maintenance.models import MaintenanceOrder
        o = MaintenanceOrder.objects.create(
            title=args['title'], description=args.get('description', ''),
            maintenance_type=args['maintenance_type'],
            priority=args.get('priority', 'normal'), scheduled_date=args.get('scheduled_date'),
            assigned_to=args.get('assigned_to'),
            cost=Decimal(args['cost']) if args.get('cost') else None,
            notes=args.get('notes', ''),
        )
        return {"id": str(o.id), "reference": o.reference, "created": True}
