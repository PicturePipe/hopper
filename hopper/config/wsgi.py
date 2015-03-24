"""
WSGI config for hopper project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
import os  # isort:skip
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

from configurations.wsgi import get_wsgi_application  # isort:skip
application = get_wsgi_application()
