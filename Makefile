install:
	pip install -r requirements_dev.txt && pre-commit install

download_models:
	wget https://gpt4all.io/models/gguf/gpt4all-falcon-q4_0.gguf -P models/ &&\
	wget https://gpt4all.io/models/gguf/all-MiniLM-L6-v2-f16.gguf -P models/

lint:
	isort --check-only . &&\
	black --check . &&\
	ruff check .

test:
	python -m pytest

all: install lint test
