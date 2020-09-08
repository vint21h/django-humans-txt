# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/__init__.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin

from humans_txt.models.thank import Thank
from humans_txt.models.person import Person
from humans_txt.admin.thank import ThankAdmin
from humans_txt.admin.person import PersonAdmin
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.component import Component
from humans_txt.admin.software import SoftwareAdmin
from humans_txt.admin.standard import StandardAdmin
from humans_txt.admin.component import ComponentAdmin


__all__ = [
    "ComponentAdmin",
    "PersonAdmin",
    "SoftwareAdmin",
    "StandardAdmin",
    "ThankAdmin",
]  # type: List[str]


# registering admin custom classes
admin.site.register(Component, ComponentAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Standard, StandardAdmin)
admin.site.register(Thank, ThankAdmin)
