from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Book

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name == "bookshelf":
        groups = {
            "Editors": ["can_edit", "can_create"],
            "Viewers": ["can_view"],
            "Admins": ["can_edit", "can_create", "can_delete"],
        }

        for group_name, permissions in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in permissions:
                try:
                    permission = Permission.objects.get(codename=perm_codename)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    print(f"Permission {perm_codename} not found")
