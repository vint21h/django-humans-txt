# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/component.py


from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "Component",
]


class Component(models.Model):
    """
    Component model.
    """

    name = models.CharField(verbose_name=_("component name"), max_length=256, db_index=True)

    class Meta:

        app_label = "humans_txt"
        verbose_name = _("component")
        verbose_name_plural = _("components")
        ordering = ["name", ]

    def __unicode__(self) -> str:

        return self.name

    def __str__(self) -> str:

        return self.__unicode__()

    def __repr__(self) -> str:

        return self.__unicode__()
