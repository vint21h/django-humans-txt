# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_standard.py


from typing import List, Optional

from django.test import TestCase

from humans_txt.models.standard import Standard


__all__: List[str] = ["StandardModelTest"]


class StandardModelTest(TestCase):
    """Standard model tests."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
        Standard.objects.create(name="PEP 8")

    def test___unicode__(self) -> None:
        """__unicode__ method must return standard name."""
        standard: Optional[Standard] = Standard.objects.first()

        self.assertEqual(first=standard.__unicode__(), second="PEP 8")  # type: ignore

    def test___repr__(self) -> None:
        """__repr__ method must return standard name."""
        standard: Optional[Standard] = Standard.objects.first()

        self.assertEqual(first=standard.__repr__(), second="PEP 8")

    def test___str__(self) -> None:
        """__str__ method must return standard name."""
        standard: Optional[Standard] = Standard.objects.first()

        self.assertEqual(first=standard.__str__(), second="PEP 8")
