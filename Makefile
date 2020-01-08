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
docker:
		docker build . -t helloworlddotnet

.PHONY: dockerrun
dockerrun:docker
		docker-compose up -d

.PHONY: dockerclean
dockerclean:
		docker-compose stop
		docker system prune -f
