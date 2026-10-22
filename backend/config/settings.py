# backend/config/settings.py
# ALL settings of the WorkMate backend live in this file.

from pathlib import Path          # makes folder paths easy
import os                         # lets us read environment variables
from dotenv import load_dotenv    # reads the .env file

# BASE_DIR = the backend folder (the one with manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Read everything from .env into memory
load_dotenv(BASE_DIR / ".env")

# Secret key comes from .env. Never write it directly in code.
SECRET_KEY = os.getenv("SECRET_KEY")

# DEBUG shows detailed errors. True only on your computer.
# .lower() == "true" turns the text "True" into a real True.
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Addresses allowed to open this backend.
# .split(",") turns "a,b" into the list ["a", "b"].
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# INSTALLED_APPS = every section the project uses
INSTALLED_APPS = [
    "django.contrib.admin",         # admin panel
    "django.contrib.auth",          # login system
    "django.contrib.contenttypes",  # Django internal helper
    "django.contrib.sessions",      # sessions
    "django.contrib.messages",      # messages
    "django.contrib.staticfiles",   # static files (CSS for admin)
    "rest_framework",               # Django REST Framework (APIs)
    "corsheaders",                  # lets the frontend call the backend
    "core",                         # OUR first app
]

# MIDDLEWARE = checkpoints every request passes through, top to bottom
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # must be first
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Frontend addresses allowed to call this API (from .env)
CORS_ALLOWED_ORIGINS = [
    o for o in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if o
]

# The file with the main address list
ROOT_URLCONF = "config.urls"

# TEMPLATES = only needed for the admin panel now
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Used by gunicorn when we deploy on Render
WSGI_APPLICATION = "config.wsgi.application"

# DATABASE: SQLite for now (a simple file, no setup needed).
# We switch to MySQL (Aiven) later, once everything else works.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Strong password rules
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# REST API settings: always answer in JSON
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}

# Language and time zone (India)
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# Static files (CSS for the admin panel)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Type of automatic ID numbers in tables
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"