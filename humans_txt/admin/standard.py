# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/standard.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["StandardAdmin"]


class StandardAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Standard model for admin area."""

    list_display: List[str] = ["name"]
    search_fields: List[str] = ["name"]
