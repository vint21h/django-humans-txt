# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/software.py


from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = ["Software"]  # type: list


class Software(models.Model):
    """
    Software model.
    """

    name = models.CharField(
        verbose_name=_("software name"), max_length=256, db_index=True
    )

    class Meta:

        app_label = "humans_txt"  # type: str
        verbose_name = _("software")  # type: str
        verbose_name_plural = _("software")  # type: str
        ordering = ["name"]  # type: list

    def __unicode__(self) -> str:

        return self.name

    def __str__(self) -> str:

        return self.__unicode__()

    def __repr__(self) -> str:

        return self.__unicode__()
