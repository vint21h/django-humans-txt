# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/conf.py


from typing import List  # pylint: disable=W0611
from datetime import date  # noqa: F401  # pylint: disable=W0611

from appconf import AppConf
from django.conf import settings


__all__ = ["settings"]  # type: List[str]


class DjangoHumansTxtAppConf(AppConf):
    """
    Django humans.txt settings.
    """

    BANNER = getattr(settings, "HUMANS_TXT_BANNER", "")  # type: str
    LAST_UPDATE = getattr(settings, "HUMANS_TXT_LAST_UPDATE", None)  # type: date
    LANGUAGES = getattr(settings, "HUMANS_TXT_LANGUAGES", None)  # type: List[str]

    class Meta:
        """
        Config settings.
        """

        prefix = "humans_txt"  # type: str
