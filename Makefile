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
		dotnet run --project Src/HelloWorld/HelloWorld/HelloWorld.csproj

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
		docker rm -f helloworld_web_1
		docker rmi helloworlddotnet
