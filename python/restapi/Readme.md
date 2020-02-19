# This is rest api to manage aks cluster on azure

## Environment variables:

- AZURE_CLIENT_ID
- AZURE_CLIENT_SECRET
- AZURE_TENANT_ID
- AZURE_SUBSCRIPTION_ID
- PUBLIC_KEY

## How to run

create credentials using command:

```
export resourceGroup=firstapp-resources

az ad sp create-for-rbac -n "http://my-app" --role contributor --scopes /subscriptions/136f4268-7dd0-446b-ab31-ec197ff147d5/resourceGroups/$
```
this creates new app in azure with full access on resourceGroup specified returns json
```
{
  "appId": “xxxxxxxxxxxxxxxxxxxx”,
  "displayName": "my-app",
  "name": "http://my-app",
  "password":  “xxxxxxxxxxxxxxxxxxxx”,
  "tenant":  “xxxxxxxxxxxxxxxxxxxx”
}
```
Configure environment variables mentioned above to .env file

Note that
- AZURE_CLIENT_ID is appId in json
- AZURE_CLIENT_SECRET is password in json
- AZURE_TENANT_ID is tenant in json
- AZURE_SUBSCRIPTION_ID can be retrieved from azure portal 

run 
`make run`


## Tests:
```
#E2E

newman run aks_poc.postman_collection.json --folder infra_apis

#unit

python3 test_aks.py
```

TODO:

- [x] Test cases
- [x] refactor and modularize
- [x] create cluster instead of single container
- [x] Multiple agent pools
- [x] C
- [x] R
- [ ] U
- [x] D
- [ ] Explore vnet creation
- [ ] Enable autoscaling
- [ ] deploy helm chart on cluster
- [ ] Automate .env file creation
- [ ] create credentials at global level and create resource_group using them


### Reference:

https://docs.microsoft.com/en-us/python/api/azure-mgmt-containerservice/azure.mgmt.containerservice.containerserviceclient?view=azure-python#managed-clusters
https://docs.microsoft.com/en-us/python/api/azure-mgmt-containerservice/azure.mgmt.containerservice.v2018_03_31.operations.managedclustersoperations?view=azure-python#methods

