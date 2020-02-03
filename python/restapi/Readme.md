# This is rest api to manage aks cluster on azure

## Tech stack:
python, flask, virtualenv

## Environment variables:

- AZURE_CLIENT_ID
- AZURE_CLIENT_SECRET
- AZURE_TENANT_ID
- AZURE_SUBSCRIPTION_ID

## How to run

Option 1

make run

Option 2

create credentials using:
`az ad sp create-for-rbac -n "http://my-app" --role contributor --scopes /subscriptions/136f4268-7dd0-446b-ab31-ec197ff147d5/resourceGroups/firstapp-resources`
this returns json 
```
{
  "appId": “xxxxxxxxxxxxxxxxxxxx”,
  "displayName": "my-app",
  "name": "http://my-app",
  "password":  “xxxxxxxxxxxxxxxxxxxx”,
  "tenant":  “xxxxxxxxxxxxxxxxxxxx”
}
```
Configure this to .env and azurermconfig.json
Note that password in json is your appSecret 

run 
`python3 myazure/instance.py -n frompython -l 'West US 2' -g firstapp-resources`




TODO:

- [ ] Fix authentication issue at azure api
- [ ] Test cases
- [ ] refactor and modularize
- [ ] create cluster instead of single container