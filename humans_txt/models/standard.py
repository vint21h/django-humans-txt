# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/standard.py


from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "Standard",
]


class Standard(models.Model):
    """
    Standard model.
    """

    name = models.CharField(verbose_name=_("standard name"), max_length=256, db_index=True)

    class Meta:

        app_label = "humans_txt"
        verbose_name = _("standard")
        verbose_name_plural = _("standards")
        ordering = ["name", ]

    def __unicode__(self) -> str:

        return self.name

    def __str__(self) -> str:

        return self.__unicode__()

    def __repr__(self) -> str:

        return self.__unicode__()
