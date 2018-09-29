# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/apps.py


from django.apps import AppConfig


__all__ = [
    "Config",
]


class Config(AppConfig):

    name = "humans_txt"
    verbose_name = "Django humans.txt"
