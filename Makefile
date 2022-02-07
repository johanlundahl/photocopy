cov:
	coverage report
	coverage html	

lint:
	flake8 --statistics --count

run:
	python3 -m photocopy.app

update: 
	git pull
	pip3 install -r requirements.txt	
