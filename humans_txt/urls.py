# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/urls.py


from typing import List, Union

from django.conf.urls import url
from django.urls.resolvers import URLPattern, URLResolver

from humans_txt.views import humans_txt


__all__: List[str] = ["urlpatterns"]


# humans.txt urls
urlpatterns: List[Union[URLPattern, URLResolver]] = [
    url(r"^$", humans_txt, name="humans-txt")
]
