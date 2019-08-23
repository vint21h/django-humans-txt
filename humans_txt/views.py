# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/views.py


from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render_to_response

from humans_txt.conf import settings
from humans_txt.models.component import Component
from humans_txt.models.person import Person
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.thank import Thank


__all__ = ["humans_txt"]  # type: list


def humans_txt(request: HttpRequest) -> HttpResponse:
    """
    Return humans.txt.

    :param request: django request instance.
    :type request: django.http.request.HttpRequest.
    :return: rendered humans.txt
    :rtype: django.http.HttpResponse.
    """

    context = {
        "BANNER": settings.HUMANS_TXT_BANNER,
        "LAST_UPDATE": settings.HUMANS_TXT_LAST_UPDATE,
        "LANGUAGES": settings.HUMANS_TXT_LANGUAGES,
        "TEAM": Person.objects.all(),
        "THANKS": Thank.objects.all(),
        "STANDARDS": Standard.objects.all(),
        "COMPONENTS": Component.objects.all(),
        "SOFTWARE": Software.objects.all(),
    }  # type: dict

    return render_to_response(
        "humans_txt/humans_txt.txt",
        context=context,
        content_type="text/plain; charset=utf-8",
    )
