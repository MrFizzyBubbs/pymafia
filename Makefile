.PHONY: all
all:

.PHONY: install
install:
	uv sync --all-extras --dev

.PHONY: format
format:
	uv run ruff check . --fix
	uv run ruff format .

.PHONY: lint
lint:
	uv run ruff check .
	uv run ruff format . --check
	uv run mypy src	

.PHONY: test
test:
	uv run pytest . -p no:faulthandler