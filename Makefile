# humans_txt
# Makefile


.ONESHELL:
PHONY: tox test twine-check twine-upload help
TEST_PYPI_URL=https://test.pypi.org/legacy/
NAME=humans_txt
EXTENSIONS=py,html,txt

tox:
	tox;\

test:
	./manage.py test $(TESTS);\

makemessages:
	cd $(NAME);\
	for locale in `ls locale`; do\
		django-admin makemessages --locale=$$locale --extension=$(EXTENSIONS);\
	done

compilemessages:
	django-admin compilemessages

twine-check:
	python setup.py bdist_wheel sdist;\
	twine check dist/*;\
	twine upload -s --repository-url $(TEST_PYPI_URL) dist/*;\

twine-upload:
	twine upload -s dist/*;\

help:
	@echo "    tox:"
	@echo "        Run tox."
	@echo "    test:"
	@echo "        Run tests, can specify tests with 'TESTS' variable."
	@echo "    makemessages:"
	@echo "        Harvest translations."
	@echo "    compilemessages:"
	@echo "        Compile translations."
	@echo "    twine-check:"
	@echo "        Run some twine checks."
	@echo "    twine-upload:"
	@echo "        Uload package to PyPi using twine."
