SHELL := /bin/bash

.PHONY: globalenv
globalenv:
	pip3 install virtualenv 

.PHONY: env
env:
	virtualenv env
	(source env/bin/activate && pip install -r requirements.txt)

.PHONY: run
run: env
run:
	flask run

.PHONY: clean
clean:
	rm -rf env
	find ./ -iname "*.pyc" -delete
