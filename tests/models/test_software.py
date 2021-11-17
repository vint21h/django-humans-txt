# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_software.py


from typing import List, Optional

from django.test import TestCase

from humans_txt.models.software import Software


__all__: List[str] = ["SoftwareModelTest"]


class SoftwareModelTest(TestCase):
    """Software model tests."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
        Software.objects.create(name="tox")

    def test___unicode__(self) -> None:
        """__unicode__ method must return software name."""
        software: Optional[Software] = Software.objects.first()

        self.assertEqual(first=software.__unicode__(), second="tox")  # type: ignore

    def test___repr__(self) -> None:
        """__repr__ method must return software name."""
        software: Optional[Software] = Software.objects.first()

        self.assertEqual(first=software.__repr__(), second="tox")

    def test___str__(self) -> None:
        """__str__ method must return software name."""
        software: Optional[Software] = Software.objects.first()

        self.assertEqual(first=software.__str__(), second="tox")
