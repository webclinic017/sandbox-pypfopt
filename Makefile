init:
	poetry config virtualenvs.in-project true
	poetry install

requirements:
	poetry export -f requirements.txt --output requirements.txt

test:
	poetry run pytest tests -v

lint:
	poetry run ruff check libs packages src tests scripts
	poetry run ruff format libs packages src tests scripts --check

format:
	poetry run ruff check libs packages src tests scripts --fix
	poetry run ruff format libs packages src tests scripts
