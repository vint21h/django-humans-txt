# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/software.py


from django.contrib import admin


__all__ = [
    "SoftwareAdmin",
]


class SoftwareAdmin(admin.ModelAdmin):
    """
    Customize Software model for admin area.
    """

    list_display = ["name", ]
    search_fields = ["name", ]
