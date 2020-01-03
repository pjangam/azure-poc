# POC on azure with azure devops, azure portal, aks


## Tech stack
- azure devops for CI
- terraform for IAC
- dotnet code 3.0 for REST api
- k8s using aks


## Steps to deploy
- Prerequisites
  - create account on dev.azure.com and portal.azure.com
  - Create Storage account `eepoctfstate` and container `tfstate` in portal.azure.com for terraform backend
  - Create Container registry `akspochelloworld` for docker image
- create new project on dev.azure.com
- In your project go to pipelines and create new pipeline. In this step you will be required to authorize github and portal.azure.com account to dev.azure.com 
- Use `build_and_push.yml` for build job. This will do following steps on our REST api code base
  - restore dependencies from Nuget
  - run unit tests 
  - create artifact for build which is getting used in other jobs (todo: remove dependencies on artifact and remove artifact)
  - build and push docker image
- Use  `InfraPipelines/create_aks_cluster.yml` for creating infrastructure. This will launch an aks cluster on portal.azure.com
- Use `deploy.yml` for deploying application to aks cluster created earlier. (todo: this step currently does docker build and push and then pull it to aks. Need to remove docker push from here.) 
- When not using application you can use `InfraPipelines/tf_destroy.yml` to destroy resources created by `InfraPipelines/create_aks_cluster.yml` and `deploy.yml`.
- Note that, `build_and_push.yml` and `create_aks_cluster.yml` are normal pipelines and can be used directly from git repo. `InfraPipelines` are created as Release pipelie and need to create manually and maintained in dev.azure.com and not in github.
  

##  Limitations/TODOs:
- [ ] Need to update `manifests/ingress.yml` manually after running `./deploy.yml` as public IP address of ingress would change after new deployment.
- [ ] Need to change helm install to upgrade.