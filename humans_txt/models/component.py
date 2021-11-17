# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/component.py


from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["Component"]


class Component(models.Model):  # noqa: DJ10,DJ11
    """Component model."""

    name = models.CharField(
        verbose_name=_("component name"), max_length=256, db_index=True
    )

    class Meta:
        """Model settings."""

        app_label: str = "humans_txt"
        verbose_name: str = _("component")
        verbose_name_plural: str = _("components")
        ordering: List[str] = ["name"]

    def __str__(self) -> str:
        """
        Model representation.

        :return: component name
        :rtype: str
        """
        return self.__unicode__()

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: component name
        :rtype: str
        """
        return self.name

    def __repr__(self) -> str:
        """
        Model representation.

        :return: component name
        :rtype: str
        """
        return self.__unicode__()
