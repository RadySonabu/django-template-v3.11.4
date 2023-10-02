"""Local settings."""
from .base import BASE_DIR, INSTALLED_APPS


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# WhiteNoise
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405

# django-debug-toolbar
INSTALLED_APPS += ["debug_toolbar"]
