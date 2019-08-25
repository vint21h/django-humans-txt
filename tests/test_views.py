# -*- coding: utf-8 -*-

# django-humans-txt
# tests/test_views.py


from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse
from django.utils import translation

from humans_txt.models.component import Component
from humans_txt.models.person import Person
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.thank import Thank
from humans_txt.views import humans_txt


__all__ = ["HumansTxtViewTest"]  # type: list


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
        Person.objects.create(
            name="Alexei Andrushievich",
            title="Backend developer",
            contact="vint21h@vint21h.pp.ua",
            twitter="https://twitter.com/vint21h/",
            location="Ukraine",
        )
        Software.objects.create(name="tox")
        Standard.objects.create(name="PEP 8")
        Thank.objects.create(
            name="Alexei Andrushievich", url="https://github.com/vint21h/"
        )

    def test_humans_txt__return_response(self) -> None:
        """
        Test view returning response.

        :return: nothing.
        :rtype: None.
        """

        request = HttpRequest()

        self.assertIsInstance(obj=humans_txt(request=request), cls=HttpResponse)

    def test_humans_txt__render__template_used(self) -> None:
        """
        Test view right template usage .

        :return: nothing.
        :rtype: None.
        """

        with translation.override("en"):
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
        Backend developer: Alexei Andrushievich
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
        """  # noqa: W605, type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("humans-txt"))

        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_BANNER"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_TEAM"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_THANKS"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_LAST_UPDATE"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_STANDARDS"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_COMPONENTS"))
        self.assertIsNotNone(obj=response.context.get("HUMANS_TXT_SOFTWARE"))
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    @override_settings(HUMANS_TXT_BANNER="")
    def test_humans_txt__render__without_banner(self) -> None:
        """
        Test view rendering result without banner.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        /* TEAM */
        Backend developer: Alexei Andrushievich
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
        """  # noqa: W605, type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("humans-txt"))

        self.assertEqual(first=response.context.get("HUMANS_TXT_BANNER"), second="")
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

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
        Backend developer: Alexei Andrushievich
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
        """  # noqa: W605, type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("humans-txt"))

        self.assertIsNone(obj=response.context.get("HUMANS_TXT_LAST_UPDATE"))
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

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
        Backend developer: Alexei Andrushievich
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
        """  # noqa: W605, type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("humans-txt"))

        self.assertListEqual(
            list1=response.context.get("HUMANS_TXT_LANGUAGES"), list2=[]
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    def test_humans_txt__render__without_team(self) -> None:
        """
        Test view rendering result without team.

        :return: nothing.
        :rtype: None.
        """

        Person.objects.all().delete()

        expected = """
             _ _                               _                                            _        _
            | (_)                             | |                                          | |      | |
          __| |_  __ _ _ __   __ _  ___ ______| |__  _   _ _ __ ___   __ _ _ __  ___ ______| |___  _| |_
         / _` | |/ _` | '_ \ / _` |/ _ \______| '_ \| | | | '_ ` _ \ / _` | '_ \/ __|______| __\ \/ / __|
        | (_| | | (_| | | | | (_| | (_) |     | | | | |_| | | | | | | (_| | | | \__ \      | |_ >  <| |_
         \__,_| |\__,_|_| |_|\__, |\___/      |_| |_|\__,_|_| |_| |_|\__,_|_| |_|___/       \__/_/\_\__|
             _/ |             __/ |
            |__/             |___/

        /* THANKS */
        Alexei Andrushievich: https://github.com/vint21h/

        /* SITE */
        Last update: 1991-08-24
        Language: en / uk
        Standards: PEP 8
        Components: Django
        Software: tox
        """  # noqa: W605, type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("humans-txt"))

        self.assertQuerysetEqual(
            qs=response.context.get("HUMANS_TXT_TEAM"), values=Person.objects.none()
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    def test_humans_txt__render__without_standards(self) -> None:
        """
        Test view rendering result without standards.

        :return: nothing.
        :rtype: None.
        """

        Standard.objects.all().delete()

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
        Backend developer: Alexei Andrushievich
        Contact: vint21h@vint21h.pp.ua
        Location: Ukraine
        Twitter: https://twitter.com/vint21h/

        /* THANKS */
        Alexei Andrushievich: https://github.com/vint21h/

        /* SITE */
        Last update: 1991-08-24
        Language: en / uk
        Components: Django
        Software: tox
        """  # noqa: W605, type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("humans-txt"))

        self.assertQuerysetEqual(
            qs=response.context.get("HUMANS_TXT_STANDARDS"),
            values=Standard.objects.none(),
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    def test_humans_txt__render__without_thanks(self) -> None:
        """
        Test view rendering result without thanks.

        :return: nothing.
        :rtype: None.
        """

        Thank.objects.all().delete()

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
        Backend developer: Alexei Andrushievich
        Contact: vint21h@vint21h.pp.ua
        Location: Ukraine
        Twitter: https://twitter.com/vint21h/

        /* SITE */
        Last update: 1991-08-24
        Language: en / uk
        Standards: PEP 8
        Components: Django
        Software: tox
        """  # noqa: W605, type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("humans-txt"))

        self.assertQuerysetEqual(
            qs=response.context.get("HUMANS_TXT_THANKS"), values=Thank.objects.none()
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    def test_humans_txt__render__without_components(self) -> None:
        """
        Test view rendering result without components.

        :return: nothing.
        :rtype: None.
        """

        Component.objects.all().delete()

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
        Backend developer: Alexei Andrushievich
        Contact: vint21h@vint21h.pp.ua
        Location: Ukraine
        Twitter: https://twitter.com/vint21h/

        /* THANKS */
        Alexei Andrushievich: https://github.com/vint21h/

        /* SITE */
        Last update: 1991-08-24
        Language: en / uk
        Standards: PEP 8
        Software: tox
        """  # noqa: W605, type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("humans-txt"))

        self.assertQuerysetEqual(
            qs=response.context.get("HUMANS_TXT_COMPONENTS"),
            values=Component.objects.none(),
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    def test_humans_txt__render__without_software(self) -> None:
        """
        Test view rendering result without software.

        :return: nothing.
        :rtype: None.
        """

        Software.objects.all().delete()

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
        Backend developer: Alexei Andrushievich
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
        """  # noqa: W605, type: str
        with translation.override("en"):
            response = self.client.get(path=reverse("humans-txt"))

        self.assertQuerysetEqual(
            qs=response.context.get("HUMANS_TXT_SOFTWARE"),
            values=Software.objects.none(),
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)
