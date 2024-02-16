"""
ASGI config for FirstWebSocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter,URLRouter
from Home.consumer import Test

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstWebSocket.settings')

application = get_asgi_application()


ws_pattern=[
    path('ws/test/', Test.as_asgi())
]

application=ProtocolTypeRouter({
    'websocket':URLRouter(ws_pattern)
})