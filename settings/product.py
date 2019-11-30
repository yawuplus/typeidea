from .base import *  # NOQA

DEBUG = False
ALLOWED_HOSTS = ['typeidea.yawujia.cn']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}
