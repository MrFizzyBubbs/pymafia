.PHONY: all
all:

.PHONY: install
install:
	poetry install

.PHONY: format
format:
	pre-commit run --all-files

.PHONY: lint
lint:
	poetry run ruff . --no-fix
	poetry run isort . --check
	poetry run black . --check
	poetry run mypy src	

.PHONY: test
test:
	poetry run pytest .