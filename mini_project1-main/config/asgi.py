"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

<<<<<<< HEAD
application =  ProtocolTypeRouter({
=======
application = ProtocolTypeRouter({
>>>>>>> 2352b3b9aa3bfc885e4bbce1998114ccfd6cf544
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
})
