from django.urls import re_path

from services import consumers

websocket_urlpatters = [
    re_path(r'ws/services/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]
