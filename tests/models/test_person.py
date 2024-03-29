# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_person.py


from typing import List, Optional

from django.test import TestCase

from humans_txt.models.person import Person


__all__: List[str] = ["PersonModelTest"]


class PersonModelTest(TestCase):
    """Person model tests."""

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Person.objects.create(
            name="Alexei Andrushievich",
            title="Backend developer",
            contact="vint21h@vint21h.pp.ua",
            twitter="https://twitter.com/vint21h/",
            location="Ukraine",
        )

    def test___unicode__(self) -> None:
        """__unicode__ method must return formatted person title and name."""
        person: Optional[Person] = Person.objects.first()

        self.assertEqual(
            first=person.__unicode__(),  # type: ignore
            second="Backend developer: Alexei Andrushievich",
        )

    def test___repr__(self) -> None:
        """__repr__ method must return formatted person title and name."""
        person: Optional[Person] = Person.objects.first()

        self.assertEqual(
            first=person.__repr__(), second="Backend developer: Alexei Andrushievich"
        )

    def test___str__(self) -> None:
        """__str__ method must return formatted person title and name."""
        person: Optional[Person] = Person.objects.first()

        self.assertEqual(
            first=person.__str__(), second="Backend developer: Alexei Andrushievich"
        )
