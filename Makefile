.PHONY: install
install:
	uv sync --all-extras --dev

.PHONY: format
format:
	uv run docformatter src --in-place
	uv run ruff check . --fix
	uv run ruff format .

.PHONY: lint
lint:
	uv run docformatter src --check
	uv run ruff check .
	uv run ruff format . --check
	uv run mypy src	

.PHONY: test
test:
	uv run pytest . -p no:faulthandler

.PHONY: check-licenses
check-licenses:
	uv pip freeze --exclude-editable > requirements.txt
	uv run licensecheck --zero