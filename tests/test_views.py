# -*- coding: utf-8 -*-

# django-humans-txt
# tests/test_views.py


from typing import List

from django.test import TestCase
from django.shortcuts import resolve_url
from django.test.utils import override_settings
from django.http import HttpRequest, HttpResponse
from django.utils.translation import override as override_translation

from humans_txt.views import humans_txt
from humans_txt.models.thank import Thank
from humans_txt.models.person import Person
from humans_txt.models.software import Software
from humans_txt.models.standard import Standard
from humans_txt.models.component import Component


__all__: List[str] = ["HumansTxtViewTest"]


class HumansTxtViewTest(TestCase):
    """humans.txt view tests."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
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
        """Test view returning response."""
        request: HttpRequest = HttpRequest()

        self.assertIsInstance(obj=humans_txt(request=request), cls=HttpResponse)

    @override_translation(language="en")
    def test_humans_txt__render__template_used(self) -> None:
        """Test view right template usage ."""
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertTemplateUsed(
            response=result, template_name="humans_txt/humans_txt.txt"
        )

    @override_translation(language="en")
    def test_humans_txt__render(self) -> None:  # noqa: CCR001
        """Test view rendering result."""
        expected: str = """
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
        """  # noqa: W605, E501
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertIsNotNone(
            obj=result.context.get("HUMANS_TXT_BANNER") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("HUMANS_TXT_TEAM") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("HUMANS_TXT_THANKS") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("HUMANS_TXT_LAST_UPDATE") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("HUMANS_TXT_STANDARDS") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("HUMANS_TXT_COMPONENTS") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("HUMANS_TXT_SOFTWARE") if result.context else None
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_settings(HUMANS_TXT_BANNER="")
    @override_translation(language="en")
    def test_humans_txt__render__without_banner(self) -> None:
        """Test view rendering result without banner."""
        expected: str = """
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
        """  # noqa: W605
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertEqual(
            first=result.context.get("HUMANS_TXT_BANNER") if result.context else None,
            second="",
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_settings(HUMANS_TXT_LAST_UPDATE=None)
    @override_translation(language="en")
    def test_humans_txt__render__without_last_update(self) -> None:
        """Test view rendering result without last update."""
        expected: str = """
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
        """  # noqa: W605, E501
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertIsNone(
            obj=result.context.get("HUMANS_TXT_LAST_UPDATE") if result.context else None
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_settings(HUMANS_TXT_LANGUAGES=[])
    @override_translation(language="en")
    def test_humans_txt__render__without_languages(self) -> None:
        """Test view rendering result without languages."""
        expected: str = """
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
        """  # noqa: W605, E501
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertListEqual(
            list1=result.context.get("HUMANS_TXT_LANGUAGES", [])  # type: ignore
            if result.context
            else [],
            list2=[],
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation(language="en")
    def test_humans_txt__render__without_team(self) -> None:
        """Test view rendering result without team."""
        Person.objects.all().delete()

        expected: str = """
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
        """  # noqa: W605, E501
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "HUMANS_TXT_TEAM", Person.objects.none()
            )
            if result.context
            else Person.objects.none(),
            values=Person.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation(language="en")
    def test_humans_txt__render__without_standards(self) -> None:
        """Test view rendering result without standards."""
        Standard.objects.all().delete()

        expected: str = """
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
        """  # noqa: W605, E501
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "HUMANS_TXT_STANDARDS", Standard.objects.none()
            )
            if result.context
            else Standard.objects.none(),
            values=Standard.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation(language="en")
    def test_humans_txt__render__without_thanks(self) -> None:
        """Test view rendering result without thanks."""
        Thank.objects.all().delete()

        expected: str = """
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
        """  # noqa: W605, E501
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "HUMANS_TXT_THANKS", Thank.objects.none()
            )
            if result.context
            else Thank.objects.none(),
            values=Thank.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation(language="en")
    def test_humans_txt__render__without_components(self) -> None:
        """Test view rendering result without components."""
        Component.objects.all().delete()

        expected: str = """
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
        """  # noqa: W605, E501
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "HUMANS_TXT_COMPONENTS", Component.objects.none()
            )
            if result.context
            else Component.objects.none(),
            values=Component.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation(language="en")
    def test_humans_txt__render__without_software(self) -> None:
        """Test view rendering result without software."""
        Software.objects.all().delete()

        expected: str = """
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
        """  # noqa: W605, E501
        result: HttpResponse = self.client.get(
            path=resolve_url(to="humans-txt")
        )

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "HUMANS_TXT_SOFTWARE", Software.objects.none()
            )
            if result.context
            else Software.objects.none(),
            values=Software.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)
