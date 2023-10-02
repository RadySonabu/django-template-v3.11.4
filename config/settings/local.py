"""Local settings."""
from .base import * # noqa:


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3", # noqa:
    }
}

# WhiteNoise
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405

# django-debug-toolbar
INSTALLED_APPS += ["debug_toolbar"]
