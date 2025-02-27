# Permissions & Groups Setup

## Custom Permissions
- `can_view` → Can view books
- `can_create` → Can create books
- `can_edit` → Can edit books
- `can_delete` → Can delete books

## Groups
- **Editors** → Can create and edit books
- **Viewers** → Can only view books
- **Admins** → Full permissions

## Usage
- Permissions enforced in views using `@permission_required()`
- Groups assigned automatically via Django signals
