# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/software.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["SoftwareAdmin"]  # type: List[str]


class SoftwareAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Software model for admin area.
    """

    list_display = ["name"]  # type: List[str]
    search_fields = ["name"]  # type: List[str]
