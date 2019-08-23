# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/urls.py


from django.conf.urls import url

from humans_txt.views import humans_txt


__all__ = ["urlpatterns"]


# humans.txt urls
urlpatterns = [url(r"^$", humans_txt, name="humans-txt")]  # type: list
