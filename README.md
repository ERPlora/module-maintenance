# Maintenance & CMMS Module

Preventive and corrective maintenance for assets and equipment.

## Features

- Create and manage maintenance work orders with reference numbers
- Three maintenance types: preventive, corrective, and predictive
- Priority-based work order management
- Schedule maintenance tasks with planned dates
- Track completion dates and maintenance costs
- Assign work orders to team members
- Maintenance scheduling for recurring tasks
- Notes field for detailed work descriptions and findings

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Maintenance & CMMS > Settings**

## Usage

Access via: **Menu > Maintenance & CMMS**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/maintenance/dashboard/` | Maintenance overview and key metrics |
| Work Orders | `/m/maintenance/work_orders/` | Create and manage maintenance work orders |
| Schedules | `/m/maintenance/schedules/` | Plan and view maintenance schedules |
| Settings | `/m/maintenance/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `MaintenanceOrder` | Work order with reference, title, description, type (preventive/corrective/predictive), priority, status, scheduled/completed dates, assignee, and cost |

## Permissions

| Permission | Description |
|------------|-------------|
| `maintenance.view_maintenanceorder` | View maintenance work orders |
| `maintenance.add_maintenanceorder` | Create new work orders |
| `maintenance.change_maintenanceorder` | Edit existing work orders |
| `maintenance.delete_maintenanceorder` | Delete work orders |
| `maintenance.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
