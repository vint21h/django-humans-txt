# -*- coding: utf-8 -*-

# django-humans-txt
# tests/settings.py


import sys
import pathlib
from datetime import date
from random import SystemRandom
from typing import Dict, List, Union


# black magic to use imports from library code
path = pathlib.Path(__file__).absolute()
project = path.parent.parent.parent
sys.path.insert(0, str(project))

# secret key
SECRET_KEY: str = "".join(
    [
        SystemRandom().choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")
        for i in range(50)
    ]
)

# configure databases
DATABASES: Dict[str, Dict[str, str]] = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

# configure templates
TEMPLATES: List[Dict[str, Union[str, List[str], bool, Dict[str, str]]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]


# add testing related apps
INSTALLED_APPS: List[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "humans_txt",
]

# configure urls
ROOT_URLCONF: str = "humans_txt.urls"

# humans.txt settings
HUMANS_TXT_BANNER: str = """
     _ _                               _                                            _        _
    | (_)                             | |                                          | |      | |
  __| |_  __ _ _ __   __ _  ___ ______| |__  _   _ _ __ ___   __ _ _ __  ___ ______| |___  _| |_
 / _` | |/ _` | '_ \ / _` |/ _ \______| '_ \| | | | '_ ` _ \ / _` | '_ \/ __|______| __\ \/ / __|
| (_| | | (_| | | | | (_| | (_) |     | | | | |_| | | | | | | (_| | | | \__ \      | |_ >  <| |_
 \__,_| |\__,_|_| |_|\__, |\___/      |_| |_|\__,_|_| |_| |_|\__,_|_| |_|___/       \__/_/\_\\__|
     _/ |             __/ |
    |__/             |___/
"""  # noqa: W605, E501
HUMANS_TXT_LAST_UPDATE: date = date(1991, 8, 24)
HUMANS_TXT_LANGUAGES: List[str] = ["en", "uk"]
