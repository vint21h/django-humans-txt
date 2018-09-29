# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/component.py


from django.contrib import admin


__all__ = [
    "ComponentAdmin",
]


class ComponentAdmin(admin.ModelAdmin):
    """
    Customize Component model for admin area.
    """

    list_display = ["name", ]
    search_fields = ["name", ]
