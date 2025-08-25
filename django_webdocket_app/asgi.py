import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_webdocket_app.settings')
django_application = get_asgi_application()

import core.routing 

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(core.routing.websocket_urlpatterns)
})