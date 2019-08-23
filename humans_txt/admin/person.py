# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/person.py


from django.contrib import admin


__all__ = ["PersonAdmin"]  # type: list


class PersonAdmin(admin.ModelAdmin):
    """
    Customize Person model for admin area.
    """

    list_display = ["name", "title", "contact", "twitter", "location"]  # type: list
    search_fields = ["name", "title", "contact", "twitter", "location"]  # type: list
