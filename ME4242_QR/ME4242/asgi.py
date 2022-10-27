"""
ASGI config for ME4242 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import user_page.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ME4242.settings")
django.setup()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            user_page.routing.websocket_urlpatterns
        )
    ),
})
#application = get_asgi_application()
