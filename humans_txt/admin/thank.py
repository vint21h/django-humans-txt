# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/thank.py


from django.contrib import admin


__all__ = ["ThankAdmin"]  # type: list


class ThankAdmin(admin.ModelAdmin):
    """
    Customize Thank model for admin area.
    """

    list_display = ["name", "url"]  # type: list
    search_fields = ["name", "url"]  # type: list
