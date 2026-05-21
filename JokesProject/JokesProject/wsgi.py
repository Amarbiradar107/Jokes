"""
WSGI config for JokesProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JokesProject.settings')

application = get_wsgi_application()
try:
	from django.conf import settings
	print('STARTUP: ALLOWED_HOSTS =', getattr(settings, 'ALLOWED_HOSTS', None))
except Exception:
	# avoid crashing the WSGI startup if logging fails
	pass
