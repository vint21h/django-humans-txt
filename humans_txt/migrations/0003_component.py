# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/migrations/0003_component.py

# Generated by Django 2.1.1 on 2018-09-29 17:56


from typing import List, Tuple

from django.db import models, migrations
from django.db.migrations.operations.base import Operation


__all__: List[str] = ["Migration"]


class Migration(migrations.Migration):
    """Migration."""

    dependencies: List[Tuple[str, str]] = [("humans_txt", "0002_standard")]

    operations: List[Operation] = [
        migrations.CreateModel(
            name="Component",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=256, verbose_name="component name"
                    ),
                ),
            ],
            options={
                "verbose_name": "component",
                "verbose_name_plural": "components",
                "ordering": ["name"],
            },
        )
    ]
