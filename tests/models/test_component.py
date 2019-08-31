# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_component.py


from typing import List  # pylint: disable=W0611

from django.test import TestCase

from humans_txt.models.component import Component


__all__ = ["ComponentModelTest"]  # type: List[str]


class ComponentModelTest(TestCase):
    """
    Component model tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """

        Component.objects.create(name="Django")

    def test___unicode__(self):
        """
        __unicode__ method must return component name.
        """

        component = Component.objects.first()  # type: Component

        self.assertEqual(first=component.__unicode__(), second="Django")

    def test___repr__(self):
        """
        __repr__ method must return component name.
        """

        component = Component.objects.first()  # type: Component

        self.assertEqual(first=component.__repr__(), second="Django")

    def test___str__(self):
        """
        __str__ method must return component name.
        """

        component = Component.objects.first()  # type: Component

        self.assertEqual(first=component.__str__(), second="Django")
