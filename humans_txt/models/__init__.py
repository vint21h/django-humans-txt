# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/__init__.py


from typing import List  # pylint: disable=W0611

from humans_txt.models.thank import Thank
from humans_txt.models.person import Person
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.component import Component


__all__ = ["Person", "Standard", "Component", "Software", "Thank"]  # type: List[str]
