# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/person.py


from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "Person",
]


class Person(models.Model):
    """
    Person model.
    """

    name = models.CharField(verbose_name=_("person name"), max_length=256, db_index=True)
    title = models.CharField(verbose_name=_("person title"), max_length=256, db_index=True)
    contact = models.CharField(verbose_name=_("person site, email, link to a contact form, etc."), max_length=256, blank=True, null=True, db_index=True)
    twitter = models.CharField(verbose_name=_("person twitter URL"), max_length=256, blank=True, null=True, db_index=True)
    location = models.CharField(verbose_name=_("person city, country"), max_length=256, blank=True, null=True, db_index=True)

    class Meta:

        app_label = "humans_txt"
        verbose_name = _("person")
        verbose_name_plural = _("persons")
        ordering = ["name", ]

    def __unicode__(self) -> str:

        return "{title}: {name}".format(**{
            "title": self.title,
            "name": self.name,
        })

    def __str__(self) -> str:

        return self.__unicode__()

    def __repr__(self) -> str:

        return self.__unicode__()
