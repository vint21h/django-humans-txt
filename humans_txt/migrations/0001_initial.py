# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/migrations/0001_initial.py

# Generated by Django 2.1.1 on 2018-09-29 16:29


from typing import List, Tuple  # pylint: disable=W0611

from django.db import models, migrations
from django.db.migrations.operations.base import Operation


class Migration(migrations.Migration):

    initial = True

    dependencies = []  # type: List[Tuple[str, str]]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                        db_index=True, max_length=256, verbose_name="person name"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=256, verbose_name="person title"
                    ),
                ),
                (
                    "contact",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=256,
                        null=True,
                        verbose_name="person site, email, link to a contact form, etc.",
                    ),
                ),
                (
                    "twitter",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=256,
                        null=True,
                        verbose_name="person twitter URL",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=256,
                        null=True,
                        verbose_name="person city, country",
                    ),
                ),
            ],
            options={
                "verbose_name": "person",
                "verbose_name_plural": "persons",
                "ordering": ["name"],
            },
        )
    ]  # type: List[Operation]
