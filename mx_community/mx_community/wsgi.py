"""
WSGI config for mx_community project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os , sys

from django.core.wsgi import get_wsgi_application
path = '/home/myusername/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mx_community.settings')

application = get_wsgi_application()
