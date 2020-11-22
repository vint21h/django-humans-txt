# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/thank.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["ThankAdmin"]  # type: List[str]


class ThankAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Thank model for admin area.
    """

    list_display = ["name", "url"]  # type: List[str]
    search_fields = ["name", "url"]  # type: List[str]
