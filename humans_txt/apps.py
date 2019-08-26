# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/apps.py


from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


__all__ = ["DjangoHumansTxtConfig"]  # type: list


class DjangoHumansTxtConfig(AppConfig):
    """
    Django humans.txt config.

    """

    name = "humans_txt"  # type: str
    verbose_name = _("Django humans.txt")  # type: str
