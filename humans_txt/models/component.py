# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/component.py


from typing import List  # pylint: disable=W0611

from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = ["Component"]  # type: List[str]


class Component(models.Model):
    """
    Component model.
    """

    name = models.CharField(
        verbose_name=_("component name"), max_length=256, db_index=True
    )

    class Meta:

        app_label = "humans_txt"  # type: str
        verbose_name = _("component")  # type: str
        verbose_name_plural = _("components")  # type: str
        ordering = ["name"]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: component name
        :rtype: str
        """

        return self.name

    def __str__(self) -> str:
        """
        Model representation.

        :return: component name
        :rtype: str
        """

        return self.__unicode__()

    def __repr__(self) -> str:
        """
        Model representation.

        :return: component name
        :rtype: str
        """

        return self.__unicode__()
