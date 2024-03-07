export show=all
export revision="head"
export mode="pleasedefine"
export t
export m
export args

test:
	poetry run coverage run -m pytest -m "not off" -x -p no:warnings --show-capture=$(show) --failed-first $(args) tests/$(t)

lint:
	poetry run ruff .

check: lint test

coverage:
	poetry run coverage report -m

coverage.html:
	poetry run coverage html --show-contexts && python -m http.server -d htmlcov 8000

run:
	poetry run python -m src
