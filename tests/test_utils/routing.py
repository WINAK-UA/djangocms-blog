# -*- coding: utf-8 -*-

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from knocker.routing import channel_routing as knocker_routing

from djangocms_blog.liveblog.routing import channel_routing as djangocms_blog_routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('knocker/', knocker_routing),
            path('liveblog/', djangocms_blog_routing),
        ])
    ),
})
