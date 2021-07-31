from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
import environ
env = environ.Env()
env.read_env(str(BASE_DIR / ".env"))

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task1',
    'task2',
    'task3',
    'django_celery_beat',
    'django_celery_results',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "pgdb",
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') 
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL') 


CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")

CELERY_RESULT_BACKEND  = 'django-db'
CELERY_CACHE_BACKEND = 'default'
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cachedb',
    }
}

CELERY_BEAT_SCHEDULE = {
    "scheduled_task":{
        "task": "task1.tasks.add",
        "schedule": 5.0,
        "args": (10,10),
    },
    "database":{
        "task": "task3.tasks.bkup",
        "schedule": 5.0,
    }
}

""" 
crontab() Execute every minute.
crontab(minute=0, hour=0) Execute daily at midnight.
crontab(minute=0, hour='*/3') Execute every three hours: midnight, 3am, 6am, 9am, noon, 3pm, 6pm, 9pm.
crontab(minute=0, hour='0,3,6,9,12,15,18,21') Same as previous.
crontab(minute='*/15') Execute every 15 minutes.
crontab(day_of_week='sunday') Execute every minute (!) at Sundays.
crontab(minute='*', hour='*', day_of_week='sun') Same as previous.
crontab(minute='*/10', hour='3,17,22', day_of_week='thu,fri') Execute every ten minutes, but only between 3-4 am, 5-6 pm, and 10-11 pm on Thursdays or Fridays.
crontab(minute=0, hour='*/2,*/3') Execute every even hour, and every hour divisible by three. This means: at every hour except: 1am, 5am, 7am, 11am, 1pm, 5pm, 7pm, 11pm
crontab(minute=0, hour='*/5') Execute hour divisible by 5. This means that it is triggered at 3pm, not 5pm (since 3pm equals the 24-hour clock value of “15”, which is divisible by 5).
crontab(minute=0, hour='*/3,8-17') Execute every hour divisible by 3, and every hour during office hours (8am-5pm).
crontab(0, 0, day_of_month='2') Execute on the second day of every month.
crontab(0, 0, day_of_month='2-30/2') Execute on every even numbered day.
crontab(0, 0, day_of_month='1-7,15-21') Execute on the first and third weeks of the month.
crontab(0, 0, day_of_month='11', month_of_year='5') Execute on the eleventh of May every year.
crontab(0, 0, month_of_year='*/3') Execute every day on the first month of every quarter.
"""