"""
Django settings for socialize_core project.
"""

import os
from pathlib import Path
import dj_database_url

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-#b)--9%(4m&0*7@7yy23pddsevteh*5ibn8oc(y^9t!5md(c+c")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True") == "True"

# Permite acesso via localhost e via subdomínio do Render/Nuvem
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",  # <-- Suporte para armazenar mídias no Cloudinary
    "django.contrib.staticfiles",
    "cloudinary",          # <-- Suporte ao Cloudinary
    "profiles",
    "posts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # Coleta e serve CSS/JS estáticos na nuvem
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "socialize_core.urls"

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

WSGI_APPLICATION = "socialize_core.wsgi.application"


# Database
# Se houver a variável DATABASE_URL (ex: Supabase/Postgres), ele usa ela.
# Caso contrário, fallback para o SQLite local.
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Configurações de Arquivos Estáticos (CSS, JS, Imagens do tema)
STATIC_URL = "/static/"

if (BASE_DIR / "static").exists():
    STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA_URL e MEDIA_ROOT
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuração do Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', ''),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY', ''),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', '')
}

# Compatibilidade antiga
STATICFILES_STORAGE = "whitenoise.storage.StaticFilesStorage"

# Força o armazenamento local de arquivos se estiver em DEBUG
if DEBUG:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.StaticFilesStorage",
        },
    }
else:
    # Produção usa Cloudinary
    STORAGES = {
        "default": {
            "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.StaticFilesStorage",
        },
    }

# Email
MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.console.EmailBackend",
    },
}

# Redirecionamentos padrão após login/logout
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'


CSRF_TRUSTED_ORIGINS = [
    'https://socialize-f6zy.onrender.com',
    'http://socialize-f6zy.onrender.com',
]