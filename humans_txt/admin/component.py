# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/component.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["ComponentAdmin"]


class ComponentAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Component model for admin area."""

    list_display: List[str] = ["name"]
    search_fields: List[str] = ["name"]
