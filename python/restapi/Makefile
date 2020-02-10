#!make
include .env
export

SHELL := /bin/bash

.PHONY: globalenv
globalenv:
	npm install -g newman
	# or brew install newman
	pip3 install virtualenv 

.PHONY: env
env:
	virtualenv env
	(source env/bin/activate && pip3 install -r requirements.txt)

.PHONY: run
run: env
run:
	flask run

.PHONY: clean
clean:
	rm -rf env
	find ./ -iname "*.pyc" -delete

.PHONY: test
test:
	nosetests --with-mocha-reporter

.PHONY: e2etest
e2etest: run
	newman run aks_poc.postman_collection.json --folder infra_apis --enviornment aks_poc.postman_environment.json

