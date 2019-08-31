# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_thank.py


from django.test import TestCase

from humans_txt.models.thank import Thank


__all__ = ["ThankModelTest"]  # type: list


class ThankModelTest(TestCase):
    """
    Thank model tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """

        Thank.objects.create(
            name="Alexei Andrushievich", url="https://github.com/vint21h/"
        )

    def test___unicode__(self):
        """
        __unicode__ method must return thank name.
        """

        thank = Thank.objects.first()  # type: Thank

        self.assertEqual(first=thank.__unicode__(), second="Alexei Andrushievich")

    def test___repr__(self):
        """
        __repr__ method must return thank name.
        """

        thank = Thank.objects.first()  # type: Thank

        self.assertEqual(first=thank.__repr__(), second="Alexei Andrushievich")

    def test___str__(self):
        """
        __str__ method must return thank name.
        """

        thank = Thank.objects.first()  # type: Thank

        self.assertEqual(first=thank.__str__(), second="Alexei Andrushievich")
