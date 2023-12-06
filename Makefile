install:
	pip install -r requirements_dev.txt && pre-commit install

lint:
	isort --check-only . &&\
	black --check . &&\
	ruff check .

test:
	python -m pytest

all: install lint test
