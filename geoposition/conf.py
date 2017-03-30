# -*- coding: utf-8 -*-
from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured


class AppSettings(object):
    defaults = {
        'MAP_WIDGET_HEIGHT': 480,
        'MAP_OPTIONS': {},
        'MARKER_OPTIONS': {},
        'GOOGLE_MAPS_API_KEY': None,
    }
    prefix = 'GEOPOSITION'

    def __init__(self, django_settings):
        self.django_settings = django_settings

    def __getattr__(self, name):
        prefixed_name = '%s_%s' % (self.prefix, name)
        if hasattr(django_settings, prefixed_name):
            return getattr(django_settings, prefixed_name)
        if name in self.defaults:
            return self.defaults[name]
        raise AttributeError("'AppSettings' object does not have a '%s' attribute" % name)


settings = AppSettings(django_settings)
