.PHONY: install

install:
	python setup.py install

.PHONY: test

test:
	$(MAKE) -C tests certs
	python -m pytest tests
