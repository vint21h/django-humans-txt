# django-humans-txt
# Makefile


.ONESHELL:
PHONY: tox test makemessages compilemessages bumpversion build check twine-check twine-upload clean help
TEST_PYPI_URL=https://test.pypi.org/legacy/
NAME=humans_txt
EXTENSIONS=py,html,txt
TRASH=build dist django_$(NAME).egg-info .tox .mypy_cache
BUILD_TYPES=bdist_wheel sdist
VERSION=`python -c "import configparser; config = configparser.ConfigParser(); config.read('setup.cfg'); print(config['metadata']['version']);"`

tox:
	tox;\

test:
	./manage.py test $(TESTS);\

makemessages:
	cd $(NAME);\
	for locale in `ls locale`; do\
		django-admin makemessages --locale=$$locale --extension=$(EXTENSIONS);\
	done;\

compilemessages:
	django-admin compilemessages;\

bumpversion:
	git tag -a $(VERSION) -m 'v$(VERSION)'

build:
	python setup.py $(BUILD_TYPES);\

check:
	pre-commit run --all-files

twine-check:
	twine check dist/*;\
	twine upload -s --repository-url $(TEST_PYPI_URL) dist/*;\

twine-upload:
	twine upload -s dist/*;\

clean:
	rm -rf $(TRASH);\
	find -type d -name __pycache__ -print0 | xargs -0 rm -rf;\

help:
	@echo "    help:"
	@echo "        Show whis help."
	@echo "    tox:"
	@echo "        Run tox."
	@echo "    test:"
	@echo "        Run tests, can specify tests with 'TESTS' variable."
	@echo "    makemessages:"
	@echo "        Harvest translations."
	@echo "    compilemessages:"
	@echo "        Compile translations."
	@echo "    bumpversion:"
	@echo "        Tag current code revision with version."
	@echo "    build:"
	@echo "    check:"
	@echo "        Perform some code checks."
	@echo "        Build python packages, can specify packages types with 'BUILD_TYPES' variable."
	@echo "    twine-check:"
	@echo "        Run some twine checks."
	@echo "    twine-upload:"
	@echo "        Uload package to PyPi using twine."
	@echo "    clean:"
	@echo "        Delete useless autogenerated files."
