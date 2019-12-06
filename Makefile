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
		docker run -d -p 5000:80 -p 5001:5001 --name helloworlddotnet helloworlddotnet

.PHONY: dockerclean
dockerclean:
		docker rm -f helloworlddotnet
		docker rmi helloworlddotnet
