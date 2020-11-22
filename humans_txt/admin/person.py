# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/person.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["PersonAdmin"]  # type: List[str]


class PersonAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Person model for admin area.
    """

    list_display = [
        "name",
        "title",
        "contact",
        "twitter",
        "location",
    ]  # type: List[str]
    search_fields = [
        "name",
        "title",
        "contact",
        "twitter",
        "location",
    ]  # type: List[str]
