# This is rest api to manage aks cluster on azure

## Environment variables:

- AZURE_CLIENT_ID
- AZURE_CLIENT_SECRET
- AZURE_TENANT_ID
- AZURE_SUBSCRIPTION_ID

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




TODO:

- [ ] Fix authentication issue at azure api
- [ ] Test cases
- [ ] refactor and modularize
- [ ] create cluster instead of single container