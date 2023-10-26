.PHONY: all
all:

.PHONY: install
install:
	poetry install

.PHONY: format
format:
	poetry run ruff check . --fix
	poetry run black .

.PHONY: lint
lint:
	poetry run ruff check .
	poetry run black . --check
	poetry run mypy src	

.PHONY: test
test:
	poetry run pytest .