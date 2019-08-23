# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/standard.py


from django.contrib import admin


__all__ = ["StandardAdmin"]  # type: list


class StandardAdmin(admin.ModelAdmin):
    """
    Customize Standard model for admin area.
    """

    list_display = ["name"]  # type: list
    search_fields = ["name"]  # type: list
