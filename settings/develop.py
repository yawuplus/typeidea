# coding:utf-8

from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 5 * 60,
        # 'OPTIONS': {
        #     'charset': 'utf8',
        # }
    }
}
INSTALLED_APPS += [
    'debug_toolbar',
    'pympler',
    'debug_toolbar_line_profiler',
    'silk',
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware',
]
INTERNAL_IPS = ['127.0.0.1']
DEBUG_TOOLBAR_PANELS = [
    # 'djdt_flamegraph.FlamegraphPanel',
    'pympler.panels.MemoryPanel',
    'debug_toolbar_line_profiler.panel.ProfilingPanel',
]
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
}
"""
Django 缓存配置
"""

"""
local-memory caching
内存缓存，线程安全，进程间独立，也就是每个进程一份缓存
"""
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
# }
"""
file system caching
文件缓存，把数据缓存到文件系统中
"""
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#     }
# }

"""
database  caching
数据库缓存，需要创建缓存用的表，这些表来存储缓存数据
"""
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }

"""
database  caching
memcached分布式缓存，(分布式逻辑在客户端)
"""
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': [
#             '139.9.95.119:11211',
#         ]
#     }
# }
#
REDIS_URL = '127.0.0.1:6379:1'
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            'PASSWORD': '',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}
