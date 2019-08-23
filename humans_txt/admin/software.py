# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/software.py


from django.contrib import admin


__all__ = ["SoftwareAdmin"]  # type: list


class SoftwareAdmin(admin.ModelAdmin):
    """
    Customize Software model for admin area.
    """

    list_display = ["name"]  # type: list
    search_fields = ["name"]  # type: list
