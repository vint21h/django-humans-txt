# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/person.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["PersonAdmin"]


class PersonAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Person model for admin area."""

    list_display: List[str] = [
        "name",
        "title",
        "contact",
        "twitter",
        "location",
    ]
    search_fields: List[str] = [
        "name",
        "title",
        "contact",
        "twitter",
        "location",
    ]
