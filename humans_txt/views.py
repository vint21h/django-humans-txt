# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/views.py


from datetime import date
from typing import Dict, List, Union  # noqa: F401

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import QuerySet
from django.http.request import HttpRequest

from humans_txt.conf import settings
from humans_txt.models.thank import Thank
from humans_txt.models.person import Person
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.component import Component


__all__: List[str] = ["humans_txt"]


def humans_txt(request: HttpRequest) -> HttpResponse:
    """
    Return humans.txt.

    :param request: django request instance
    :type request: HttpRequest
    :return: rendered humans.txt
    :rtype: HttpResponse
    """
    context: Dict[
        str,
        Union[
            str,
            date,
            List[str],
            QuerySet[Person],
            QuerySet[Thank],
            QuerySet[Standard],
            QuerySet[Component],
            QuerySet[Software],
        ],
    ] = {
        "HUMANS_TXT_BANNER": settings.HUMANS_TXT_BANNER,
        "HUMANS_TXT_LAST_UPDATE": settings.HUMANS_TXT_LAST_UPDATE,
        "HUMANS_TXT_LANGUAGES": settings.HUMANS_TXT_LANGUAGES,
        "HUMANS_TXT_TEAM": Person.objects.all(),
        "HUMANS_TXT_THANKS": Thank.objects.all(),
        "HUMANS_TXT_STANDARDS": Standard.objects.all(),
        "HUMANS_TXT_COMPONENTS": Component.objects.all(),
        "HUMANS_TXT_SOFTWARE": Software.objects.all(),
    }

    return render(
        request=request,
        template_name="humans_txt/humans_txt.txt",
        context=context,
        content_type="text/plain; charset=utf-8",
    )
