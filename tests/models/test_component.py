# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_component.py


from typing import List, Optional  # pylint: disable=W0611

from django.test import TestCase

from humans_txt.models.component import Component


__all__ = ["ComponentModelTest"]  # type: List[str]


class ComponentModelTest(TestCase):
    """
    Component model tests.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        """
        Set up non-modified objects used by all test methods.
        """

        Component.objects.create(name="Django")

    def test___unicode__(self) -> None:
        """
        __unicode__ method must return component name.
        """

        component = Component.objects.first()  # type: Optional[Component]

        self.assertEqual(first=component.__unicode__(), second="Django")  # type: ignore

    def test___repr__(self) -> None:
        """
        __repr__ method must return component name.
        """

        component = Component.objects.first()  # type: Optional[Component]

        self.assertEqual(first=component.__repr__(), second="Django")

    def test___str__(self) -> None:
        """
        __str__ method must return component name.
        """

        component = Component.objects.first()  # type: Optional[Component]

        self.assertEqual(first=component.__str__(), second="Django")
