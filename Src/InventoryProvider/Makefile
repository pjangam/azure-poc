reponame := akspochelloworld

.PHONY: login
login:
	echo $(acrpassword) | docker login $(reponame).azurecr.io -u $(acruser) --password-stdin


.PHONY: all
## Runs unit the tests.
all:test

.PHONY: clean
clean:
	dotnet clean -c Release

.PHONY: build
build:
	dotnet build -c Release

.PHONY: test
test:
	dotnet test -c Release

.PHONY: start
start:
	#sudo npm i -g pm2
	pm2 start apps.json

.PHONY:stop
stop:
	pm2 stop apps.json
	pm2 delete apps.json

.PHONY: publish
publish:
	dotnet publish -c Release -o out

.PHONY: docker
docker:login
docker:
	docker build . -t $(reponame).azurecr.io/inventory-provider:latest -t $(reponame).azurecr.io/inventory-provider:0.0.1
	docker push $(reponame).azurecr.io/inventory-provider:latest

.PHONY: dockerrun
dockerrun:docker
	docker-compose up -d

.PHONY: dockerclean
dockerclean:
	docker-compose stop
	docker system prune -f

-include User.mk
-include ../User.mk
-include ../../User.mk
-include ~/User.mk
