"""Production Settings."""
from .base import * # noqa:


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {
            "options": "-c search_path=django-template-3.11.4",
        },
        "NAME": os.getenv("DB_NAME"), # noqa:
        "USER": os.getenv("DB_USER"), # noqa:
        "PASSWORD": os.getenv("DB_PASSWORD"), # noqa:
        "HOST": os.getenv("DB_HOST"), # noqa:
        "PORT": "5432",
    }
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
