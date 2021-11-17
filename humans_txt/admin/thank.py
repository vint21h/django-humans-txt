# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/thank.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["ThankAdmin"]


class ThankAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Thank model for admin area."""

    list_display: List[str] = ["name", "url"]
    search_fields: List[str] = ["name", "url"]
