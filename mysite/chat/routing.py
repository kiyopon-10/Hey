# from django.urls import re_path
from django.urls import path

from . import consumers

# websocket_urlpatterns = [
#     re_path(r'', consumers.ChatConsumer.as_asgi()),
# ]

websocket_urlpatterns = [
    path("<str:roomCode>", consumers.ChatConsumer.as_asgi())
]