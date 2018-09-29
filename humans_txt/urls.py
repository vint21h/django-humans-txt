# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/urls.py


from django.conf.urls import url


__all__ = [
    "urlpatterns",
]


app_name = "humans_txt"
# humans.txt urls
urlpatterns = [
    url(r"^$", lambda x: x, name="humans_txt"),
]
