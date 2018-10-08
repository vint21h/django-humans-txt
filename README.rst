.. django-humans-txt
.. README.rst

A django-humans-txt documentation
=================================

    *django-humans-txt is a django reusable application to handle humans.txt (http://humanstxt.org/)*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``git clone https://github.com/vint21h/django-humans-txt.git``. Or download the latest release from https://github.com/vint21h/django-humans-txt/tags/.
* Run ``python ./setup.py install`` from the repository source tree or the unpacked archive. Or use pip: ``pip install django-humans-txt``.

Configuration
-------------
Add ``"humans_txt"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS += (
        "humans_txt",
    )

Add ``"humans_txt"`` to your urls definitions.

.. code-block:: python

    urlpatterns += [
        url(r"^humans\.txt", include("humans_txt.urls")),
    )

Include ``"humans_txt/includes/humans_txt_meta.html"`` in your base template rel meta tag to ``<head>`` html tag .

For example:

.. code-block:: django

    <head>
        {% include "humans_txt/includes/humans_txt_meta.html" %}
    </head>

Run ``python manage.py migrate`` in your project folder to apply app migrations.

Usage
-----
Just fill Django humans.txt models instances in your admin in your taste.

Settings
--------
``HUMANS_TXT_BANNER``
    Contains an banner that placed at the start of humans.txt response. Defaults to ``""``.
``HUMANS_TXT_LAST_UPDATE``
    Contains project last update date. Defaults to ``None``.
``HUMANS_TXT_LANGUAGES``
    Contains list of site supported languages. Defaults to ``None``.

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
