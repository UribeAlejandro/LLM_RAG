install:
	pip install -r requirements_dev.txt && pre-commit install

test:
	python -m pytest

all: install test
