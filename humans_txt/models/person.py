# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/person.py


from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["Person"]


class Person(models.Model):  # noqa: DJ10,DJ11
    """Person model."""

    name = models.CharField(
        verbose_name=_("person name"), max_length=256, db_index=True
    )
    title = models.CharField(
        verbose_name=_("person title"), max_length=256, db_index=True
    )
    contact = models.CharField(  # noqa: DJ01
        verbose_name=_("person site, email, link to a contact form, etc."),
        max_length=256,
        blank=True,
        null=True,
        db_index=True,
    )
    twitter = models.CharField(  # noqa: DJ01
        verbose_name=_("person twitter URL"),
        max_length=256,
        blank=True,
        null=True,
        db_index=True,
    )
    location = models.CharField(  # noqa: DJ01
        verbose_name=_("person city, country"),
        max_length=256,
        blank=True,
        null=True,
        db_index=True,
    )

    class Meta:
        """Model settings."""

        app_label: str = "humans_txt"
        verbose_name: str = _("person")
        verbose_name_plural: str = _("persons")
        ordering: List[str] = ["name"]

    def __str__(self) -> str:
        """
        Model representation.

        :return: formatted string with person title and name
        :rtype: str
        """
        return self.__unicode__()

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: formatted string with person title and name
        :rtype: str
        """
        return f"{self.title}: {self.name}"

    def __repr__(self) -> str:
        """
        Model representation.

        :return: formatted string with person title and name
        :rtype: str
        """
        return self.__unicode__()
