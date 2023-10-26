.PHONY: all
all:

.PHONY: install
install:
	poetry install

.PHONY: format
format:
	poetry run ruff check . --fix
	poetry run ruff format .

.PHONY: lint
lint:
	poetry run ruff check .
	poetry run ruff format . --check
	poetry run mypy src	

.PHONY: test
test:
	poetry run pytest .