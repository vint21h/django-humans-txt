# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_component.py


from django.test import TestCase

from humans_txt.models.component import Component


__all__ = ["ComponentModelTest"]  # type: list


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

        component = Component.objects.first()

        self.assertEqual(component.__unicode__(), "Django")

    def test___repr__(self):
        """
        __repr__ method must return component name.
        """

        component = Component.objects.first()

        self.assertEqual(component.__repr__(), "Django")

    def test___str__(self):
        """
        __str__ method must return component name.
        """

        component = Component.objects.first()

        self.assertEqual(component.__str__(), "Django")
