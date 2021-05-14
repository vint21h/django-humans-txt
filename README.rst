.. django-humans-txt
.. README.rst


A django-humans-txt documentation
=================================

|GitHub|_ |Coveralls|_ |pypi-license|_ |pypi-version|_ |pypi-python-version|_ |pypi-django-version|_ |pypi-format|_ |pypi-wheel|_ |pypi-status|_

    *django-humans-txt is a Django reusable application to handle humans.txt (http://humanstxt.org/)*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``$ git clone https://github.com/vint21h/django-humans-txt.git``. Or download the latest release from https://github.com/vint21h/django-humans-txt/tags/.
* Run ``$ python ./setup.py install`` from the repository source tree or the unpacked archive. Or use pip: ``$ pip install django-humans-txt``.

Configuration
-------------
* Add ``"humans_txt"`` to ``settings.INSTALLED_APPS``:

.. code-block:: python

    # settings.py

    INSTALLED_APPS += [
        "humans_txt",
    ]

* Add ``"humans_txt"`` to your URLs definitions:

.. code-block:: python

    # urls.py

    from django.urls import re_path


    urlpatterns += [
        re_path(r"^humans\.txt", include("humans_txt.urls")),
    ]

* Run ``$ python ./manage.py migrate`` in your project folder to apply app migrations.

Settings
--------
``HUMANS_TXT_BANNER``
    Contains a banner that placed at the start of humans.txt response. Defaults to ``""``.
``HUMANS_TXT_LAST_UPDATE``
    Contains project last update date. Defaults to ``None``.
``HUMANS_TXT_LANGUAGES``
    Contains list of site supported languages. Defaults to ``None``.

Usage
-----
* Include ``"humans_txt/includes/humans_txt_meta.html"`` in your base template rel meta tag to ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    <head>
        {% include "humans_txt/includes/humans_txt_meta.html" %}
    </head>

* Just fill Django humans.txt models instances in your admin in your taste.

Licensing
---------
django-humans-txt is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (a
t your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-humans-txt/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.

.. |GitHub| image:: https://github.com/vint21h/django-humans-txt/workflows/build/badge.svg
    :alt: GitHub
.. |Coveralls| image:: https://coveralls.io/repos/github/vint21h/django-humans-txt/badge.svg?branch=master
    :alt: Coveralls
.. |pypi-license| image:: https://img.shields.io/pypi/l/django-humans-txt
    :alt: License
.. |pypi-version| image:: https://img.shields.io/pypi/v/django-humans-txt
    :alt: Version
.. |pypi-django-version| image:: https://img.shields.io/pypi/djversions/django-humans-txt
    :alt: Supported Django version
.. |pypi-python-version| image:: https://img.shields.io/pypi/pyversions/django-humans-txt
    :alt: Supported Python version
.. |pypi-format| image:: https://img.shields.io/pypi/format/django-humans-txt
    :alt: Package format
.. |pypi-wheel| image:: https://img.shields.io/pypi/wheel/django-humans-txt
    :alt: Python wheel support
.. |pypi-status| image:: https://img.shields.io/pypi/status/django-humans-txt
    :alt: Package status
.. _GitHub: https://github.com/vint21h/django-humans-txt/actions/
.. _Coveralls: https://coveralls.io/github/vint21h/django-humans-txt?branch=master
.. _pypi-license: https://pypi.org/project/django-humans-txt/
.. _pypi-version: https://pypi.org/project/django-humans-txt/
.. _pypi-django-version: https://pypi.org/project/django-humans-txt/
.. _pypi-python-version: https://pypi.org/project/django-humans-txt/
.. _pypi-format: https://pypi.org/project/django-humans-txt/
.. _pypi-wheel: https://pypi.org/project/django-humans-txt/
.. _pypi-status: https://pypi.org/project/django-humans-txt/
