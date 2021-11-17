# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_component.py


from typing import List, Optional

from django.test import TestCase

from humans_txt.models.component import Component


__all__: List[str] = ["ComponentModelTest"]


class ComponentModelTest(TestCase):
    """Component model tests."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
        Component.objects.create(name="Django")

    def test___unicode__(self) -> None:
        """__unicode__ method must return component name."""
        component: Optional[Component] = Component.objects.first()

        self.assertEqual(first=component.__unicode__(), second="Django")  # type: ignore

    def test___repr__(self) -> None:
        """__repr__ method must return component name."""
        component: Optional[Component] = Component.objects.first()

        self.assertEqual(first=component.__repr__(), second="Django")

    def test___str__(self) -> None:
        """__str__ method must return component name."""
        component: Optional[Component] = Component.objects.first()

        self.assertEqual(first=component.__str__(), second="Django")
