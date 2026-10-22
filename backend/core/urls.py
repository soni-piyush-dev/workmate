# backend/core/urls.py
# The address list of the "core" app.

from django.urls import path   # path() links an address to a view
from . import views            # "." means: this same folder

urlpatterns = [
    # address "health/" runs the health() function
    path("health/", views.health, name="health"),
]