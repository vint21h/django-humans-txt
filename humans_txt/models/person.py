# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/person.py


from typing import List  # pylint: disable=W0611

from django.db import models
from django.utils.translation import gettext_lazy as _


__all__ = ["Person"]  # type: List[str]


class Person(models.Model):
    """
    Person model.
    """

    name = models.CharField(
        verbose_name=_("person name"), max_length=256, db_index=True
    )
    title = models.CharField(
        verbose_name=_("person title"), max_length=256, db_index=True
    )
    contact = models.CharField(
        verbose_name=_("person site, email, link to a contact form, etc."),
        max_length=256,
        blank=True,
        null=True,
        db_index=True,
    )
    twitter = models.CharField(
        verbose_name=_("person twitter URL"),
        max_length=256,
        blank=True,
        null=True,
        db_index=True,
    )
    location = models.CharField(
        verbose_name=_("person city, country"),
        max_length=256,
        blank=True,
        null=True,
        db_index=True,
    )

    class Meta:
        """
        Model settings.
        """

        app_label = "humans_txt"  # type: str
        verbose_name = _("person")  # type: str
        verbose_name_plural = _("persons")  # type: str
        ordering = ["name"]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: formatted string with person title and name
        :rtype: str
        """

        return f"{self.title}: {self.name}"

    def __str__(self) -> str:
        """
        Model representation.

        :return: formatted string with person title and name
        :rtype: str
        """

        return self.__unicode__()

    def __repr__(self) -> str:
        """
        Model representation.

        :return: formatted string with person title and name
        :rtype: str
        """

        return self.__unicode__()
