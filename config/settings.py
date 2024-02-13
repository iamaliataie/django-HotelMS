"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&gk6^^*v3z59q(l$yo5o@&2mn76w&0-v!w9*u#k$&(!lfn8w8a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom apps
    'account.apps.AccountConfig',
    'hotel.apps.HotelConfig',
    'user_dashboard.apps.UserDashboardConfig',
    'addon.apps.AddonConfig',

    # Third party apps
    'taggit',
    'import_export',
    'mathfilters',
    'crispy_forms',
    'ckeditor_uploader',
    'django_ckeditor_5',
    
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    'site_header': 'Hotel Management System',
    'site_brand': 'Hotel Management',
    'copyright': 'All Rights Reserved 2024',
    'welcome_sign': 'Welcome to HMS Django',
    'topmenu_links': [
        {'name': 'Home', 'url': 'admin:index', 'permission': ['auth.view_user']},
        {'name': 'Company', 'url': '/admin/addons/company/'},
        {'name': 'Users', 'url': '/admin/userauth/uer/'},
        
        {'model': 'AUTH_USER_MODEL.User'}
    ],
    'order_with_respect_to':[
        'hotel',
        'hotel.Hotel',
        'hotel.Room',
        'hotel.Booking',
        'hotel.BookingDetail',
        'hotel.Guest',
        'hotel.RoomServices',
        'account',
        'addons',
    ],
    'icons': {
        'admin.LogEntry': 'fas fa-file',
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'account.User': 'fas fa-user',
        'account.Profile': 'fas fa-address-card',
        'hotel.Hotel': 'fas fa-th',
        'hotel.Booking': 'fas fa-calendar-week',
        'hotel.BookingDetail': 'fas fa-calendar-alt',
        'hotel.Guest': 'fas fa-user',
        'hotel.Room': 'fas fa-bed',
        'hotel.RoomServices': 'fas fa-user-cog',
        'hotel.Notification': 'fas fa-bell',
        'hotel.Coupon': 'fas fa-tag',
        'hotel.Bookmark': 'fas fa-heart'
    },
    'show_ui_builder': True
}

JAZZMIN_UI_TWEAKS = {
    'navbar_small_text': False,
    'footer_small_text': False,
    'body_small_text': True,
    'brand_small_text': False,
    'brand_colour': 'navbar-indigo',
    'accent': 'accent-olive',
    'navbar': 'navbar-indigo nabvar-dark',
    'no_navbar_border': False,
    'navbar_fixed': False,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': False,
    'sidebar': 'sidebar-dark-indigo',
    'sidebar_nav_small_text': False,
    'sibar_disable_expand': False,
    'sidebar_nav_child_indent': False,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_flat_style': False,
    'sidebar_nav_legacy_style': False,
    'theme': 'cyborg',
    'dark_mode_theme': 'cyborg',
    'button_classes': {
        'primary': 'btn-primary',
        'secondary': 'btn-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-success'
    }
}