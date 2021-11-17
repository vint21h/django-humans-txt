# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/software.py


from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["Software"]


class Software(models.Model):  # noqa: DJ10,DJ11
    """Software model."""

    name = models.CharField(
        verbose_name=_("software name"), max_length=256, db_index=True
    )

    class Meta:
        """Model settings."""

        app_label: str = "humans_txt"
        verbose_name: str = _("software")
        verbose_name_plural: str = _("software")
        ordering: List[str] = ["name"]

    def __str__(self) -> str:
        """
        Model representation.

        :return: software name
        :rtype: str
        """
        return self.__unicode__()

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: software name
        :rtype: str
        """
        return self.name

    def __repr__(self) -> str:
        """
        Model representation.

        :return: software name
        :rtype: str
        """
        return self.__unicode__()
