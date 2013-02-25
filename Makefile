.PHONY: clean doc doc-clean tests check test install build bdist

build:
	python setup.py build

bdist:
	python setup.py build --executable="/usr/bin/env python"
	python setup.py bdist --formats=egg

install:
	python setup.py install

clean: doc-clean
	rm -rf build/;\
	find . -name "*.egg-info" | xargs rm -rf;\
	rm -rf dist/;\
	find . -name "*.pyc" | xargs rm -f;
	rm -f nosetests.xml

doc:
	sphinx-apidoc -o doc/ src/ && cd doc/ && make html
doc-clean:
	cd doc && rm -rf _templates _static _build searchindex.js objects.inv

test:
	nosetests --with-xunit tests -v

tests: test
check: test
