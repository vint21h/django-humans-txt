# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/standard.py


from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["Standard"]


class Standard(models.Model):  # noqa: DJ10,DJ11
    """Standard model."""

    name = models.CharField(
        verbose_name=_("standard name"), max_length=256, db_index=True
    )

    class Meta:
        """Model settings."""

        app_label: str = "humans_txt"
        verbose_name: str = _("standard")
        verbose_name_plural: str = _("standards")
        ordering: List[str] = ["name"]

    def __str__(self) -> str:
        """
        Model representation.

        :return: standard name
        :rtype: str
        """
        return self.__unicode__()

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: standard name
        :rtype: str
        """
        return self.name

    def __repr__(self) -> str:
        """
        Model representation.

        :return: standard name
        :rtype: str
        """
        return self.__unicode__()
