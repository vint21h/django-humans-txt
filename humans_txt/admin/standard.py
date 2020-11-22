# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/standard.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["StandardAdmin"]  # type: List[str]


class StandardAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Standard model for admin area.
    """

    list_display = ["name"]  # type: List[str]
    search_fields = ["name"]  # type: List[str]
