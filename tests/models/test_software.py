# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_software.py


from django.test import TestCase

from humans_txt.models.software import Software


__all__ = ["SoftwareModelTest"]  # type: list


class SoftwareModelTest(TestCase):
    """
    Software model tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """

        Software.objects.create(name="tox")

    def test___unicode__(self):
        """
        __unicode__ method must return software name.
        """

        software = Software.objects.first()

        self.assertEqual(software.__unicode__(), "tox")

    def test___repr__(self):
        """
        __repr__ method must return software name.
        """

        software = Software.objects.first()

        self.assertEqual(software.__repr__(), "tox")

    def test___str__(self):
        """
        __str__ method must return software name.
        """

        software = Software.objects.first()

        self.assertEqual(software.__str__(), "tox")
