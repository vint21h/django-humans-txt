# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/views.py


from typing import Dict, List, Union  # noqa: F401, pylint: disable=W0611

from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render_to_response

from humans_txt.conf import settings
from humans_txt.models.component import Component
from humans_txt.models.person import Person
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.thank import Thank


__all__ = ["humans_txt"]  # type: List[str]


def humans_txt(request: HttpRequest) -> HttpResponse:
    """
    Return humans.txt.

    :param request: django request instance.
    :type request: django.http.request.HttpRequest.
    :return: rendered humans.txt
    :rtype: django.http.HttpResponse.
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
    }  # noqa: E501 type: Dict[str, Union[str, List[str], Person, Thank, Standard, Component, Software]]

    return render_to_response(
        "humans_txt/humans_txt.txt",
        context=context,
        content_type="text/plain; charset=utf-8",
    )
