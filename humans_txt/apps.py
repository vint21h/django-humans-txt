# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/apps.py


from typing import List  # pylint: disable=W0611

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__ = ["DjangoHumansTxtConfig"]  # type: List[str]


class DjangoHumansTxtConfig(AppConfig):
    """
    Django humans.txt config.
    """

    name = "humans_txt"  # type: str
    verbose_name = _("Django humans.txt")  # type: str
