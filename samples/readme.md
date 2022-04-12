# Sample Apps 

## Tools required

Instalation on Ubuntu 20

[DotNet Core SDK](https://docs.microsoft.com/en-us/dotnet/core/install/linux-ubuntu)

```
sudo snap install dotnet-sdk --classic --channel=6.0
sudo snap alias dotnet-sdk.dotnet dotnet
```

[Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt)

```
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

[Docker](https://docs.docker.com/engine/install/ubuntu/) 

```
sudo apt-get install docker.io

```


## DotNet Core


```
dotnet init webapp 
dotnet build
dotnet run
```

Dockerfile

```
# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY *.csproj ./
RUN dotnet restore

# Copy everything else and build
COPY ../engine/examples ./
RUN dotnet publish -c Release -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY --from=build-env /app/out .
ENTRYPOINT ["dotnet", "aspnetapp.dll"]

```



## Java Site using Maven

```
mvn archetype:generate -DgroupId=com.circlek.web -DartifactId=java-web-project -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
```


## Spring Boot App

```
https://start.spring.io/


```


##Dockerfiles




##Push image to Azure Container Registry

```

az login
az acr login --name [registry_name]
az acr build --registry [registry_name] --image nginx --file Dockerfile .

```

# NGINX 

(NGINX Tutorial)[https://docs.microsoft.com/en-us/azure/container-registry/container-registry-tutorial-quick-task]