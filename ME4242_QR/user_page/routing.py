from django.urls import re_path
from . import game_controller

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', game_controller.Controller.as_asgi()),
]