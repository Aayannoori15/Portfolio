from pathlib import Path
import os
from urllib.parse import urlparse, unquote
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
DEBUG = os.getenv("DEBUG", "False") == "True"

default_allowed_hosts = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
    '.vercel.app',
]
allowed_hosts_env = os.getenv('ALLOWED_HOSTS')
ALLOWED_HOSTS = (
    [host.strip() for host in allowed_hosts_env.split(',') if host.strip()]
    if allowed_hosts_env
    else default_allowed_hosts
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'personalweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'home' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'personalweb.wsgi.application'

DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise ImproperlyConfigured(
        "DATABASE_URL is required and must point to PostgreSQL."
    )

parsed = urlparse(DATABASE_URL)
if parsed.scheme not in {"postgres", "postgresql"}:
    raise ImproperlyConfigured(
        "Unsupported DATABASE_URL scheme. Use PostgreSQL, for example: "
        "postgresql://user:password@host:5432/dbname"
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': unquote(parsed.path.lstrip('/')),
        'USER': unquote(parsed.username or ''),
        'PASSWORD': unquote(parsed.password or ''),
        'HOST': parsed.hostname or '',
        'PORT': str(parsed.port or 5432),
        'OPTIONS': {
            'sslmode': os.getenv('PGSSLMODE', 'require'),
        },
    }
}
# ===== CLOUDINARY CONFIG =====
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# ===== STATIC & MEDIA =====
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / 'home' / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

default_csrf_trusted_origins = [
    'http://localhost',
    'http://127.0.0.1',
    'https://*.onrender.com',
    'https://*.vercel.app',
]
csrf_trusted_origins_env = os.getenv('CSRF_TRUSTED_ORIGINS')
CSRF_TRUSTED_ORIGINS = (
    [origin.strip() for origin in csrf_trusted_origins_env.split(',') if origin.strip()]
    if csrf_trusted_origins_env
    else default_csrf_trusted_origins
)

# ===== PASSWORD VALIDATORS =====
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
