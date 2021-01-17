# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/thank.py


from typing import List  # pylint: disable=W0611

from django.db import models
from django.utils.translation import gettext_lazy as _


__all__ = ["Thank"]  # type: List[str]


class Thank(models.Model):
    """
    Thank model.
    """

    name = models.CharField(
        verbose_name=_("thank to person or organization name"),
        max_length=256,
        db_index=True,
    )
    url = models.URLField(
        verbose_name=_("thank to person or organization site URL"),
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
        verbose_name = _("thank")  # type: str
        verbose_name_plural = _("thanks")  # type: str
        ordering = ["name"]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: thank to name
        :rtype: str
        """

        return self.name

    def __str__(self) -> str:
        """
        Model representation.

        :return: thank to name
        :rtype: str
        """

        return self.__unicode__()

    def __repr__(self) -> str:
        """
        Model representation.

        :return: thank to name
        :rtype: str
        """

        return self.__unicode__()
