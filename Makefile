install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	

refactor: format lint

test:
	python -m pytest -vv test.py



all: install lint test format 
