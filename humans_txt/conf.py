# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/conf.py


from typing import List
from datetime import date  # noqa: F401

from appconf import AppConf
from django.conf import settings


__all__: List[str] = ["settings"]


class DjangoHumansTxtAppConf(AppConf):
    """Django humans.txt settings."""

    BANNER: str = getattr(settings, "HUMANS_TXT_BANNER", "")
    LAST_UPDATE: date = getattr(settings, "HUMANS_TXT_LAST_UPDATE", None)
    LANGUAGES: List[str] = getattr(settings, "HUMANS_TXT_LANGUAGES", None)

    class Meta:
        """Config settings."""

        prefix: str = "humans_txt"
