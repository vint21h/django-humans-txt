# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/views.py


from datetime import date

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.db.models import QuerySet
try:
    from django.core.urlresolvers import reverse
except ModuleNotFoundError:
    from django.urls import reverse

from humans_txt import settings
from humans_txt.models.component import Component
from humans_txt.models.person import Person
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.thank import Thank


__all__ = [
    "humans_txt",
]


def humans_txt(request: HttpRequest) -> HttpResponse:
    """
    Return humans.txt.

    :param request: django request instance.
    :type request: django.http.request.HttpRequest.
    :return: rendered humans.txt
    :rtype: django.http.HttpResponse.
    """

    context = {
        "BANNER": settings.BANNER,  # type: str
        "LAST_UPDATE": settings.LAST_UPDATE,  # type: date
        "LANGUAGES": settings.LANGUAGES,  # type: list
        "TEAM": Person.objects.all(),  # type: QuerySet
        "THANKS": Thank.objects.all(),  # type: QuerySet
        "STANDARDS": Standard.objects.all(),  # type: QuerySet
        "COMPONENTS": Component.objects.all(),  # type: QuerySet
        "SOFTWARE": Software.objects.all(),  # type: QuerySet
    }  # type: dict

    return render_to_response("humans_txt/humans_txt.txt", context=context, content_type="text/plain; charset=utf-8")
