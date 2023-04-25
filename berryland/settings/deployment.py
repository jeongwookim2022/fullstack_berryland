# ##################.env SETTINGS##############################
from .base_settings import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)
############################################################


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True # True is for Local Development.
DEBUG = False

# #################### ALLOWING HOSTS from other devices ##############
# ################### FOR Mobile users ################################
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'rlawjddn12',
        'HOST': 'mariadb',  # DB container name
        'PORT': '3306',
    }
}


######################################################
CSRF_TRUSTED_ORIGINS = ['http://70.34.213.95/']

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_REPLACE_HTTPS_REFERER = True

CORS_ORIGIN_WHITELIST = (
    'http://70.34.213.95/'
)

#########################################################