

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'abc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


STRIPE_PUB_KEY = 'pk_test_51IVMBZEot1lBvM8YE7wS4DE1xsNVfuP0aFFx0V6DsQVLtizwdeCs4LoLEMk2W7fO9uVAhbe588PgBkCkWBsWhpa100DQBHQFmV'
STRIPE_SECRET_KEY = 'sk_test_51IVMBZEot1lBvM8YCX3hhDZbCW8bulmIXLYAuptI5rrZJTPYejDwMKY2kS5WD8l6KxTWL2sa5TFjsHwAzttoMJWb00HaVtEGLI'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'crispy_forms',

    # 'myapps',
    'social_project.social_app',
    'social_project.social_profile',
    'social_project.feed',
    'social_project.social_conversation',
    'social_project.social_notification',
    #eco
    'ecommerce_project.ecommerce_app',
    'ecommerce_project.eco_vendor',
    'ecommerce_project.eco_product',
    'ecommerce_project.eco_cart',
    'ecommerce_project.eco_order',

    #time track
    'time_track_project.time_track',
    'time_track_project.time_profile',
    'time_track_project.time_team',
    'time_track_project.time_task',
    'time_track_project.time_dashboard',

    ##
    'my_info',


]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGOUT_REDIRECT_URL = 'homepage'
LOGIN_URL = 'social-login'
LOGIN_REDIRECT_URL = 'homepage'

#for cart
SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_projects.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_project.social_notification.context_processors.notifications',
                'ecommerce_project.eco_product.context_processors.menu_category',
                'ecommerce_project.eco_cart.context_processors.cart',
                'time_track_project.time_track.context_processors.active_team',
                'time_track_project.time_task.context_processors.active_entry'

            ],
        },
    },
]

WSGI_APPLICATION = 'my_projects.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
 
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'my_projects/my_static']

STATIC_ROOT = Path(BASE_DIR,'static/')


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


## CREATING A EMAIL HOST
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT =587
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = 'testnilldiggonto@gmail.com'
EMAIL_HOST_PASSWORD = ''
DEFAULT_EMAIL_FROM = 'Time <testnilldiggonto@gmail.com>'
# ACCEPTION_URL  = ''