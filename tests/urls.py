# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('test_django_cookie_app.urls', namespace='test_django_cookie_app')),
]
