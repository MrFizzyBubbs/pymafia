.PHONY: all
all:

.PHONY: install
install:
	poetry install

.PHONY: format
format:
	poetry run ruff . --fix
	poetry run isort .
	poetry run black .

.PHONY: lint
lint:
	poetry run ruff .
	poetry run isort . --check
	poetry run black . --check
	poetry run mypy src	

.PHONY: test
test:
	poetry run pytest .