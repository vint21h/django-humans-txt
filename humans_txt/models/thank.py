# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/thank.py


from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["Thank"]


class Thank(models.Model):  # noqa: DJ10,DJ11
    """Thank model."""

    name = models.CharField(
        verbose_name=_("thank to person or organization name"),
        max_length=256,
        db_index=True,
    )
    url = models.URLField(  # noqa: DJ01
        verbose_name=_("thank to person or organization site URL"),
        max_length=256,
        blank=True,
        null=True,
        db_index=True,
    )

    class Meta:
        """Model settings."""

        app_label: str = "humans_txt"
        verbose_name: str = _("thank")
        verbose_name_plural: str = _("thanks")
        ordering: List[str] = ["name"]

    def __str__(self) -> str:
        """
        Model representation.

        :return: thank to name
        :rtype: str
        """
        return self.__unicode__()

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: thank to name
        :rtype: str
        """
        return self.name

    def __repr__(self) -> str:
        """
        Model representation.

        :return: thank to name
        :rtype: str
        """
        return self.__unicode__()
