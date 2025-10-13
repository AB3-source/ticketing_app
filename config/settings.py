import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
=======
SECRET_KEY = 'your-secret-key-here'
>>>>>>> c78360f (Added RegisterView and serializer for JWT authentication)
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
<<<<<<< HEAD
    'accounts',
    'tickets',
=======
    'rest_framework_simplejwt',
    'tickets',  # your tickets app
>>>>>>> c78360f (Added RegisterView and serializer for JWT authentication)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

<<<<<<< HEAD
ROOT_URLCONF = 'ticketing_app.urls'
=======
ROOT_URLCONF = 'config.urls'
>>>>>>> c78360f (Added RegisterView and serializer for JWT authentication)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

<<<<<<< HEAD
WSGI_APPLICATION = 'ticketing_app.wsgi.application'

# Database (using SQLite for Week 1)
=======
WSGI_APPLICATION = 'config.wsgi.application'

# Database
>>>>>>> c78360f (Added RegisterView and serializer for JWT authentication)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Accra'
USE_I18N = True
USE_TZ = True

<<<<<<< HEAD
# Static files
STATIC_URL = '/static/'
=======
# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
>>>>>>> c78360f (Added RegisterView and serializer for JWT authentication)

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

<<<<<<< HEAD
# Custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# REST Framework & JWT configuration
=======
# Custom User model
AUTH_USER_MODEL = False  # Assuming you created a custom User model in tickets.models

# DRF + JWT settings
>>>>>>> c78360f (Added RegisterView and serializer for JWT authentication)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
<<<<<<< HEAD
=======
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
>>>>>>> c78360f (Added RegisterView and serializer for JWT authentication)
}
