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


deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 181371422128.dkr.ecr.us-east-1.amazonaws.com	
	docker build -t todo_app .
	docker tag todo_app:latest 181371422128.dkr.ecr.us-east-1.amazonaws.com/todo_app:latest
	docker push 181371422128.dkr.ecr.us-east-1.amazonaws.com/todo_app:latest


all: install lint test format deploy
