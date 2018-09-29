# -*- coding: utf-8 -*-

# 
# humans_txt/apps.py


from __future__ import unicode_literals

from django.apps import AppConfig


__all__ = ["Config", ]


class Config(AppConfig):

    name = "humans_txt"
    verbose_name = "Django humans.txt"
