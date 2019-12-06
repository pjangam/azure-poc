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
## Runs the unit tests.
test:
	dotnet test -c Release

.PHONY: start
## Starts the backend.
start:
	dotnet run --project Src/HelloWorld/HelloWorld/HelloWorld.csproj 

