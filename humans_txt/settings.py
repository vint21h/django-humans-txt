# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/settings.py


from django.conf import settings


__all__ = [
    "BANNER",
]


BANNER = getattr(settings, "HUMANS_TXT_BANNER", "")
