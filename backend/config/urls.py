# backend/config/urls.py
# MAIN address list. It sends addresses to each app.

from django.contrib import admin
from django.urls import path, include  # include() = "look inside another urls.py"

urlpatterns = [
    path("admin/", admin.site.urls),     # admin panel at /admin/
    path("api/", include("core.urls")),  # everything under /api/ goes to core
]