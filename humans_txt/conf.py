# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/conf.py


from datetime import date  # noqa: F401

from appconf import AppConf
from django.conf import settings


__all__ = ["settings"]  # type: list


class DjangoHumansTxtAppConf(AppConf):
    """
    Django humans.txt settings.
    """

    BANNER = getattr(settings, "HUMANS_TXT_BANNER", "")  # type: str
    LAST_UPDATE = getattr(settings, "HUMANS_TXT_LAST_UPDATE", None)  # type: date
    LANGUAGES = getattr(settings, "HUMANS_TXT_LANGUAGES", None)  # type: list

    class Meta:

        prefix = "humans_txt"  # type: str
