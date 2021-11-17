# -*- coding: utf-8 -*-

# django-humans-txt
# tests/models/test_thank.py


from typing import List, Optional

from django.test import TestCase

from humans_txt.models.thank import Thank


__all__: List[str] = ["ThankModelTest"]


class ThankModelTest(TestCase):
    """Thank model tests."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
        Thank.objects.create(
            name="Alexei Andrushievich", url="https://github.com/vint21h/"
        )

    def test___unicode__(self) -> None:
        """__unicode__ method must return thank name."""
        thank: Optional[Thank] = Thank.objects.first()

        self.assertEqual(
            first=thank.__unicode__(), second="Alexei Andrushievich"  # type: ignore
        )

    def test___repr__(self) -> None:
        """__repr__ method must return thank name."""
        thank: Optional[Thank] = Thank.objects.first()

        self.assertEqual(first=thank.__repr__(), second="Alexei Andrushievich")

    def test___str__(self) -> None:
        """__str__ method must return thank name."""
        thank: Optional[Thank] = Thank.objects.first()

        self.assertEqual(first=thank.__str__(), second="Alexei Andrushievich")
