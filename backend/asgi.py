from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from room.websocket.routing import ws_urlpatterns
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
from .middleware import TokenAuthMiddleware


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            TokenAuthMiddleware(URLRouter(
                ws_urlpatterns 
            )
            )
        ),
    })