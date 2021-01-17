# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/software.py


from typing import List  # pylint: disable=W0611

from django.db import models
from django.utils.translation import gettext_lazy as _


__all__ = ["Software"]  # type: List[str]


class Software(models.Model):
    """
    Software model.
    """

    name = models.CharField(
        verbose_name=_("software name"), max_length=256, db_index=True
    )

    class Meta:
        """
        Model settings.
        """

        app_label = "humans_txt"  # type: str
        verbose_name = _("software")  # type: str
        verbose_name_plural = _("software")  # type: str
        ordering = ["name"]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: software name
        :rtype: str
        """

        return self.name

    def __str__(self) -> str:
        """
        Model representation.

        :return: software name
        :rtype: str
        """
        return self.__unicode__()

    def __repr__(self) -> str:
        """
        Model representation.

        :return: software name
        :rtype: str
        """

        return self.__unicode__()
