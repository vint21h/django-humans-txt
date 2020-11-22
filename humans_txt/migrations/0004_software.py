# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/migrations/0004_software.py

# Generated by Django 2.1.1 on 2018-09-29 18:06


from typing import List, Tuple  # pylint: disable=W0611

from django.db import models, migrations
from django.db.migrations.operations.base import Operation


class Migration(migrations.Migration):

    dependencies = [("humans_txt", "0003_component")]  # type: List[Tuple[str, str]]

    operations = [
        migrations.CreateModel(
            name="Software",
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
                        db_index=True, max_length=256, verbose_name="software name"
                    ),
                ),
            ],
            options={
                "verbose_name": "software",
                "verbose_name_plural": "software",
                "ordering": ["name"],
            },
        )
    ]  # type: List[Operation]
