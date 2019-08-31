# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/urls.py


from typing import List, Union  # pylint: disable=W0611

from django.conf.urls import url
from django.urls.resolvers import URLPattern, URLResolver  # pylint: disable=W0611

from humans_txt.views import humans_txt


__all__ = ["urlpatterns"]


# humans.txt urls
urlpatterns = [
    url(r"^$", humans_txt, name="humans-txt")
]  # type: List[Union[URLPattern, URLResolver]]
