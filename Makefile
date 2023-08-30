init:
	poetry config virtualenvs.in-project true
	poetry install

requirements:
	poetry export -f requirements.txt --output requirements.txt

test:
	poetry run pytest tests -v

black:
	poetry run black src/ scripts/ tests/

isort:
	poetry run isort src/ scripts/ tests/

flake8:
	poetry run flake8 src/ scripts/ tests/

format: black isort
