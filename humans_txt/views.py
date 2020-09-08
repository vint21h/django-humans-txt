# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/views.py


from datetime import date
from typing import Dict, List, Union  # noqa: F401  # pylint: disable=W0611

from django.shortcuts import render
from django.db.models import Manager
from django.http import HttpResponse
from django.http.request import HttpRequest

from humans_txt.conf import settings
from humans_txt.models.thank import Thank
from humans_txt.models.person import Person
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.component import Component


__all__ = ["humans_txt"]  # type: List[str]


def humans_txt(request: HttpRequest) -> HttpResponse:
    """
    Return humans.txt.

    :param request: django request instance
    :type request: HttpRequest
    :return: rendered humans.txt
    :rtype: HttpResponse
    """

    context = {
        "HUMANS_TXT_BANNER": settings.HUMANS_TXT_BANNER,
        "HUMANS_TXT_LAST_UPDATE": settings.HUMANS_TXT_LAST_UPDATE,
        "HUMANS_TXT_LANGUAGES": settings.HUMANS_TXT_LANGUAGES,
        "HUMANS_TXT_TEAM": Person.objects.all(),
        "HUMANS_TXT_THANKS": Thank.objects.all(),
        "HUMANS_TXT_STANDARDS": Standard.objects.all(),
        "HUMANS_TXT_COMPONENTS": Component.objects.all(),
        "HUMANS_TXT_SOFTWARE": Software.objects.all(),
    }  # type: Dict[str, Union[str, date, List[str], Manager[Person], Manager[Thank], Manager[Standard], Manager[Component], Manager[Software]]]  # noqa: E501

    return render(
        request=request,
        template_name="humans_txt/humans_txt.txt",
        context=context,
        content_type="text/plain; charset=utf-8",
    )
