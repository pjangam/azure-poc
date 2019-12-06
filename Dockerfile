FROM  mcr.microsoft.com/dotnet/core/sdk:3.1
COPY Src Src
COPY Makefile Makefile
COPY helloworld.sln helloworld.sln
RUN dotnet publish -c Release -o out
# RUN rm -rf Src
EXPOSE 5000
EXPOSE 5001
# CMD out/HelloWorld
CMD dotnet run --project Src/HelloWorld/HelloWorld/HelloWorld.csproj
