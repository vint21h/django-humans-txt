# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/views.py


from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http.request import HttpRequest
try:
    from django.core.urlresolvers import reverse
except ModuleNotFoundError:
    from django.urls import reverse

from humans_txt import settings


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
        "BANNER": settings.BANNER,
        "LAST_UPDATE": settings.LAST_UPDATE,
    }  # type: dict

    return render_to_response("humans_txt/humans_txt.txt", context=context, content_type="text/plain")
