#"$schema" = "https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#"

#"contentVersion" = "1.0.0.0"

parameters "resourceName" {
  "value" = "manual-akl-cluster"
}

parameters "location" {
  "value" = "eastus"
}

parameters "dnsPrefix" {
  "value" = "manual-akl-cluster-dns"
}

parameters "agentCount" {
  "value" = 1
}

"parameters" "agentVMSize" {
  "value" = "Standard_DS2_v2"
}

"parameters" "servicePrincipalClientId" {
  "value" = 
}

"parameters" "servicePrincipalClientSecret" {
  "value" = 
}

"parameters" "kubernetesVersion" {
  "value" = "1.13.12"
}

"parameters" "networkPlugin" {
  "value" = "azure"
}

"parameters" "enableRBAC" {
  "value" = true
}

"parameters" "aadSessionKey" {
  "value" = 
}

"parameters" "enableHttpApplicationRouting" {
  "value" = true
}

"parameters" "vmssNodePool" {
  "value" = true
}

"parameters" "vnetSubnetID" {
  "value" = "/subscriptions/f66a2d2c-ddff-4567-9f0d-5ff84db7e238/resourceGroups/manual-rg/providers/Microsoft.Network/virtualNetworks/manual-rg-vnet/subnets/default"
}

"parameters" "serviceCidr" {
  "value" = "10.0.0.0/16"
}

"parameters" "dnsServiceIP" {
  "value" = "10.0.0.10"
}

"parameters" "dockerBridgeCidr" {
  "value" = "172.17.0.1/16"
}

"parameters" "principalId" {
  "value" = "1368db23-4f75-4c31-ac55-19c7294271ab"
}

"parameters" "workspaceName" {
  "value" = "mnualWorkspace"
}

"parameters" "omsWorkspaceId" {
  "value" = "/subscriptions/f66a2d2c-ddff-4567-9f0d-5ff84db7e238/resourceGroups/DefaultResourceGroup-EUS/providers/Microsoft.OperationalInsights/workspaces/mnualWorkspace"
}

"parameters" "workspaceRegion" {
  "value" = "eastus"
}