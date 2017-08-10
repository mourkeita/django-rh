"""
WSGI config for rh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append("/home/khidma/dev/django-rh/rh")
from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rh.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rh.settings")

application = get_wsgi_application()
