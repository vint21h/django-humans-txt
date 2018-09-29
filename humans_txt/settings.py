# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/settings.py


from datetime import date

from django.conf import settings


__all__ = [
    "BANNER",
    "LAST_UPDATE",
    "LANGUAGES",
]


BANNER = getattr(settings, "HUMANS_TXT_BANNER", "")  # type: str
LAST_UPDATE = getattr(settings, "HUMANS_TXT_LAST_UPDATE", None)  # type: date
LANGUAGES = getattr(settings, "HUMANS_TXT_LANGUAGES", None)  # type: list
