"""URLS for user app."""
from django.urls import path
from .views import indexRate


urlpatterns = [path("", indexRate, name="index")]
