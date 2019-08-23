# -*- coding: utf-8 -*-

# django-humans-txt
# tests/test_views.py


from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse

from humans_txt.views import humans_txt
from humans_txt.models.component import Component
from humans_txt.models.person import Person
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.thank import Thank


__all__ = [
    "HumansTxtViewTest",
]  # type: list


class HumansTxtViewTest(TestCase):
    """
    humans.txt view tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """

        Component.objects.create(name="Django")
        Person.objects.create(name="Alexei Andrushievich", title="Python developer", contact="vint21h@vint21h.pp.ua", twitter="https://twitter.com/vint21h/", location="Ukraine")
        Software.objects.create(name="tox")
        Standard.objects.create(name="PEP 8")
        Thank.objects.create(name="Alexei Andrushievich", url="https://github.com/vint21h/")

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

        expected = """
             _ _                               _                                            _        _   
            | (_)                             | |                                          | |      | |  
          __| |_  __ _ _ __   __ _  ___ ______| |__  _   _ _ __ ___   __ _ _ __  ___ ______| |___  _| |_ 
         / _` | |/ _` | '_ \ / _` |/ _ \______| '_ \| | | | '_ ` _ \ / _` | '_ \/ __|______| __\ \/ / __|
        | (_| | | (_| | | | | (_| | (_) |     | | | | |_| | | | | | | (_| | | | \__ \      | |_ >  <| |_ 
         \__,_| |\__,_|_| |_|\__, |\___/      |_| |_|\__,_|_| |_| |_|\__,_|_| |_|___/       \__/_/\_\__|
             _/ |             __/ |                                                                      
            |__/             |___/                                                                       

        /* TEAM */       
        Python developer: Alexei Andrushievich
        Contact: vint21h@vint21h.pp.ua
        Location: Ukraine
        Twitter: https://twitter.com/vint21h/

        /* THANKS */
        Alexei Andrushievich: https://github.com/vint21h/

        /* SITE */
        Last update: 1991-08-24
        Language: en / uk
        Standards: PEP 8
        Components: Django
        Software: tox
        """  # type: str
        response = self.client.get(
            path=reverse("humans-txt")
        )

        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_BANNER"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_TEAM"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_THANKS"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_LAST_UPDATE"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_STANDARDS"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_COMPONENTS"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_SOFTWARE"))
        self.assertInHTML(needle=expected, haystack=response.content.decode())

    @override_settings(HUMANS_TXT_BANNER="")
    def test_humans_txt__render__without_banner(self) -> None:
        """
        Test view rendering result without banner.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        /* TEAM */       
        Python developer: Alexei Andrushievich
        Contact: vint21h@vint21h.pp.ua
        Location: Ukraine
        Twitter: https://twitter.com/vint21h/

        /* THANKS */
        Alexei Andrushievich: https://github.com/vint21h/

        /* SITE */
        Last update: 1991-08-24
        Language: en / uk
        Standards: PEP 8
        Components: Django
        Software: tox
        """  # type: str
        response = self.client.get(
            path=reverse("humans-txt")
        )

        self.assertEqual(first="", second=response.context.get("HUMANS_TXT_BANNER"))
        self.assertInHTML(needle=expected, haystack=response.content.decode())

    @override_settings(HUMANS_TXT_LAST_UPDATE=None)
    def test_humans_txt__render__without_last_update(self) -> None:
        """
        Test view rendering result without last update.

        :return: nothing.
        :rtype: None.
        """

        expected = """
             _ _                               _                                            _        _   
            | (_)                             | |                                          | |      | |  
          __| |_  __ _ _ __   __ _  ___ ______| |__  _   _ _ __ ___   __ _ _ __  ___ ______| |___  _| |_ 
         / _` | |/ _` | '_ \ / _` |/ _ \______| '_ \| | | | '_ ` _ \ / _` | '_ \/ __|______| __\ \/ / __|
        | (_| | | (_| | | | | (_| | (_) |     | | | | |_| | | | | | | (_| | | | \__ \      | |_ >  <| |_ 
         \__,_| |\__,_|_| |_|\__, |\___/      |_| |_|\__,_|_| |_| |_|\__,_|_| |_|___/       \__/_/\_\__|
             _/ |             __/ |                                                                      
            |__/             |___/                                                                       

        /* TEAM */       
        Python developer: Alexei Andrushievich
        Contact: vint21h@vint21h.pp.ua
        Location: Ukraine
        Twitter: https://twitter.com/vint21h/

        /* THANKS */
        Alexei Andrushievich: https://github.com/vint21h/

        /* SITE */
        Language: en / uk
        Standards: PEP 8
        Components: Django
        Software: tox
        """  # type: str
        response = self.client.get(
            path=reverse("humans-txt")
        )

        self.assertIsNone(obj=response.context.get("HUMANS_TXT_LAST_UPDATE"))
        self.assertInHTML(needle=expected, haystack=response.content.decode())

    @override_settings(HUMANS_TXT_LANGUAGES=[])
    def test_humans_txt__render__without_languages(self) -> None:
        """
        Test view rendering result without languages.

        :return: nothing.
        :rtype: None.
        """

        expected = """
             _ _                               _                                            _        _   
            | (_)                             | |                                          | |      | |  
          __| |_  __ _ _ __   __ _  ___ ______| |__  _   _ _ __ ___   __ _ _ __  ___ ______| |___  _| |_ 
         / _` | |/ _` | '_ \ / _` |/ _ \______| '_ \| | | | '_ ` _ \ / _` | '_ \/ __|______| __\ \/ / __|
        | (_| | | (_| | | | | (_| | (_) |     | | | | |_| | | | | | | (_| | | | \__ \      | |_ >  <| |_ 
         \__,_| |\__,_|_| |_|\__, |\___/      |_| |_|\__,_|_| |_| |_|\__,_|_| |_|___/       \__/_/\_\__|
             _/ |             __/ |                                                                      
            |__/             |___/                                                                       

        /* TEAM */       
        Python developer: Alexei Andrushievich
        Contact: vint21h@vint21h.pp.ua
        Location: Ukraine
        Twitter: https://twitter.com/vint21h/

        /* THANKS */
        Alexei Andrushievich: https://github.com/vint21h/

        /* SITE */
        Last update: 1991-08-24
        Standards: PEP 8
        Components: Django
        Software: tox
        """  # type: str
        response = self.client.get(
            path=reverse("humans-txt")
        )

        self.assertListEqual(list1=[], list2=response.context.get("HUMANS_TXT_LANGUAGES"))
        self.assertInHTML(needle=expected, haystack=response.content.decode())
