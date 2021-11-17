# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/software.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["SoftwareAdmin"]


class SoftwareAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Software model for admin area."""

    list_display: List[str] = ["name"]
    search_fields: List[str] = ["name"]
