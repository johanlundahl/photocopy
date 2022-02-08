cov:
	coverage report
	coverage html	

lint:
	flake8 --statistics --count

run:
	python3 -m photocopy.app

test:
	coverage run --source=. -m pytest tests/*_test.py 

update: 
	git pull
	pip3 install -r requirements.txt	

