from django.urls import path
from app.channels.consumer import OBSControlWebSocketConsumer


websocket_urlpatterns = [
    path('ws/obs_control/', OBSControlWebSocketConsumer.as_asgi()),
]
