"""Apps for user app."""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """User config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
