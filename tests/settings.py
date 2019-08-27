# -*- coding: utf-8 -*-

# django-humans-txt
# tests/settings.py


from datetime import date
import pathlib
import sys


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY = "django-humans-txt-test-key"  # type: str

# configure databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "django-humans-txt-tests.sqlite3",
    }
}  # type: dict

# configure templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]  # type: list


# add testing related apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django_nose",
    "humans_txt",
]  # type: list

# add nose test runner
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"  # type: str

# configure nose test runner
NOSE_ARGS = [
    "--rednose",
    "--force-color",
    "--with-timer",
    "--with-doctest",
    "--with-coverage",
    "--cover-inclusive",
    "--cover-erase",
    "--cover-package=humans_txt",
    "--logging-clear-handlers",
]  # type: list

# configure urls
ROOT_URLCONF = "humans_txt.urls"  # type: str

# humans.txt settings
HUMANS_TXT_BANNER = """
     _ _                               _                                            _        _
    | (_)                             | |                                          | |      | |
  __| |_  __ _ _ __   __ _  ___ ______| |__  _   _ _ __ ___   __ _ _ __  ___ ______| |___  _| |_
 / _` | |/ _` | '_ \ / _` |/ _ \______| '_ \| | | | '_ ` _ \ / _` | '_ \/ __|______| __\ \/ / __|
| (_| | | (_| | | | | (_| | (_) |     | | | | |_| | | | | | | (_| | | | \__ \      | |_ >  <| |_
 \__,_| |\__,_|_| |_|\__, |\___/      |_| |_|\__,_|_| |_| |_|\__,_|_| |_|___/       \__/_/\_\\__|
     _/ |             __/ |
    |__/             |___/
"""  # noqa: W605, E501, type: str
HUMANS_TXT_LAST_UPDATE = date(1991, 8, 24)  # type: date
HUMANS_TXT_LANGUAGES = ["en", "uk"]  # type: list
