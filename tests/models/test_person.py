# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_person.py


from django.test import TestCase

from humans_txt.models.person import Person


__all__ = ["PersonModelTest"]  # type: list


class PersonModelTest(TestCase):
    """
    Person model tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """

        Person.objects.create(
            name="Alexei Andrushievich",
            title="Backend developer",
            contact="vint21h@vint21h.pp.ua",
            twitter="https://twitter.com/vint21h/",
            location="Ukraine",
        )

    def test___unicode__(self):
        """
        __unicode__ method must return formatted person title and name.
        """

        person = Person.objects.first()

        self.assertEqual(
            person.__unicode__(), "Backend developer: Alexei Andrushievich"
        )

    def test___repr__(self):
        """
        __repr__ method must return formatted person title and name.
        """

        person = Person.objects.first()

        self.assertEqual(person.__repr__(), "Backend developer: Alexei Andrushievich")

    def test___str__(self):
        """
        __str__ method must return formatted person title and name.
        """

        person = Person.objects.first()

        self.assertEqual(person.__str__(), "Backend developer: Alexei Andrushievich")
