ruff:
	uv run ruff format
	uv run ruff check --fix

pytest:
	uv run pytest --cov=src --cov-report=html -v

mypy:
	uv run mypy . --strict
