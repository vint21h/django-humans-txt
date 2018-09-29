# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/standard.py


from django.contrib import admin


__all__ = [
    "StandardAdmin",
]


class StandardAdmin(admin.ModelAdmin):
    """
    Customize Standard model for admin area.
    """

    list_display = ["name", ]
    search_fields = ["name", ]
