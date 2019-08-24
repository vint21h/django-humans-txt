# django-humans-txt
# Makefile

docs:
	rst2html README.rst > index.html && zip docs.zip index.html

clear:
	rm -rf index.html docs.zip build dist django_humans_txt.egg-info

build:
	./setup.py bdist_wheel sdist

register:
	./setup.py bdist_wheel sdist register

upload:
	./setup.py bdist_wheel sdist upload
