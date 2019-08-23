# -*- coding: utf-8 -*-

# django-humans-txt
# settings/settings.py


import pathlib
import sys


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY = "django-humans-txt-test-key"  # type: str

# configure databases
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "django-humans-txt-tests.sqlite3"}
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


# add nose test runner application and humans_txt
INSTALLED_APPS = ["django_nose", "humans_txt"]  # type: list

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
