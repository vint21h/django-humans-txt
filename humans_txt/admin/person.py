# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/person.py


from django.contrib import admin


__all__ = [
    "PersonAdmin",
]


class PersonAdmin(admin.ModelAdmin):
    """
    Customize Person model for admin area.
    """

    list_display = ["name", "title", "contact", "twitter", "location", ]
    search_fields = ["name", "title", "contact", "twitter", "location", ]
