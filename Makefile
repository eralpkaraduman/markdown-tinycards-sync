init:
	pip install -r requirements.txt

test:
	nosetests tests

sync:
	python -m sample