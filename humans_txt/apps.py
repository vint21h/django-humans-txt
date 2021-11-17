# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/apps.py


from typing import List

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["DjangoHumansTxtConfig"]


class DjangoHumansTxtConfig(AppConfig):
    """Django humans.txt config."""

    name: str = "humans_txt"
    verbose_name: str = _("Django humans.txt")
