# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/component.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["ComponentAdmin"]  # type: List[str]


class ComponentAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Component model for admin area.
    """

    list_display = ["name"]  # type: List[str]
    search_fields = ["name"]  # type: List[str]
