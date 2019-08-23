# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/apps.py


from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


__all__ = ["DjangoHumansTxtConfig"]  # type: list


class DjangoHumansTxtConfig(AppConfig):

    name = "humans_txt"
    verbose_name = _("Django humans.txt")
