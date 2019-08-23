# -*- coding: utf-8 -*-

# django-humans-txt
# tests/test_views.py


import json

from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse

from humans_txt.views import humans_txt


__all__ = [
    "HumansTxtViewTest",
]  # type: list


class HumansTxtViewTest(TestCase):
    """
    humans.txt view tests.
    """

    def test_humans_txt__return_response(self) -> None:
        """
        Test view returning response.

        :return: nothing.
        :rtype: None.
        """

        request = HttpRequest()

        self.assertIsInstance(
            obj=humans_txt(request=request), cls=HttpResponse
        )

    def test_humans_txt__render__template_used(self) -> None:
        """
        Test view right template usage .

        :return: nothing.
        :rtype: None.
        """

        response = self.client.get(path=reverse("humans-txt"))

        self.assertTemplateUsed(
            response=response, template_name="humans_txt/humans_txt.txt"
        )

    def test_humans_txt__render(self) -> None:
        """
        Test view rendering result.

        :return: nothing.
        :rtype: None.
        """

        expected = """"""  # type: str
        response = self.client.get(
            path=reverse("humans-txt")
        ).content.decode()  # type: str

        self.assertInHTML(needle=expected, haystack=response)

    @override_settings(HUMANS_TXT_BANNER="")
    def test_humans_txt__render__without_banner(self) -> None:
        """
        Test view rendering result without banner.

        :return: nothing.
        :rtype: None.
        """

        expected = """"""  # type: str
        response = self.client.get(
            path=reverse("humans-txt")
        ).content.decode()  # type: str

        self.assertInHTML(needle=expected, haystack=response)

    @override_settings(HUMANS_TXT_LAST_UPDATE="")
    def test_humans_txt__render__without_last_update(self) -> None:
        """
        Test view rendering result without last update.

        :return: nothing.
        :rtype: None.
        """

        expected = """"""  # type: str
        response = self.client.get(
            path=reverse("humans-txt")
        ).content.decode()  # type: str

        self.assertInHTML(needle=expected, haystack=response)

    @override_settings(HUMANS_TXT_LAST_LANGUAGES="")
    def test_humans_txt__render__without_languages(self) -> None:
        """
        Test view rendering result without languages.

        :return: nothing.
        :rtype: None.
        """

        expected = """"""  # type: str
        response = self.client.get(
            path=reverse("humans-txt")
        ).content.decode()  # type: str

        self.assertInHTML(needle=expected, haystack=response)
