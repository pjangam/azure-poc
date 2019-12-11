#"$schema" = "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"

#"contentVersion" = "1.0.0.0"

"parameters" "resourceName" {
  "type" = "string"

  "metadata" = {
    "description" = "The name of the Managed Cluster resource."
  }
}

"parameters" "location" {
  "type" = "string"

  "metadata" = {
    "description" = "The location of AKS resource."
  }
}

"parameters" "dnsPrefix" {
  "type" = "string"

  "metadata" = {
    "description" = "Optional DNS prefix to use with hosted Kubernetes API server FQDN."
  }
}

"parameters" "osDiskSizeGB" {
  "type" = "int"

  "defaultValue" = 0

  "metadata" = {
    "description" = "Disk size (in GiB) to provision for each of the agent pool nodes. This value ranges from 0 to 1023. Specifying 0 will apply the default disk size for that agentVMSize."
  }

  "minValue" = 0

  "maxValue" = 1023
}

"parameters" "agentCount" {
  "type" = "int"

  "defaultValue" = 3

  "metadata" = {
    "description" = "The number of agent nodes for the cluster."
  }

  "minValue" = 1

  "maxValue" = 100
}

"parameters" "agentVMSize" {
  "type" = "string"

  "defaultValue" = "Standard_D2_v2"

  "metadata" = {
    "description" = "The size of the Virtual Machine."
  }
}

"parameters" "servicePrincipalClientId" {
  "metadata" = {
    "description" = "Client ID (used by cloudprovider)."
  }

  "type" = "securestring"
}

"parameters" "servicePrincipalClientSecret" {
  "metadata" = {
    "description" = "The Service Principal Client Secret."
  }

  "type" = "securestring"
}

"parameters" "aadSessionKey" {
  "type" = "securestring"
}

"parameters" "osType" {
  "type" = "string"

  "defaultValue" = "Linux"

  "allowedValues" = ["Linux"]

  "metadata" = {
    "description" = "The type of operating system."
  }
}

"parameters" "kubernetesVersion" {
  "type" = "string"

  "defaultValue" = "1.7.7"

  "metadata" = {
    "description" = "The version of Kubernetes."
  }
}

"parameters" "networkPlugin" {
  "type" = "string"

  "allowedValues" = ["azure", "kubenet"]

  "metadata" = {
    "description" = "Network plugin used for building Kubernetes network."
  }
}

"parameters" "maxPods" {
  "type" = "int"

  "defaultValue" = 30

  "metadata" = {
    "description" = "Maximum number of pods that can run on a node."
  }
}

"parameters" "enableRBAC" {
  "type" = "bool"

  "defaultValue" = true

  "metadata" = {
    "description" = "Boolean flag to turn on and off of RBAC."
  }
}

"parameters" "vmssNodePool" {
  "type" = "bool"

  "defaultValue" = false

  "metadata" = {
    "description" = "Boolean flag to turn on and off of VM scale sets"
  }
}

"parameters" "windowsProfile" {
  "type" = "bool"

  "defaultValue" = false

  "metadata" = {
    "description" = "Boolean flag to turn on and off of VM scale sets"
  }
}

"parameters" "enableHttpApplicationRouting" {
  "type" = "bool"

  "defaultValue" = true

  "metadata" = {
    "description" = "Boolean flag to turn on and off of http application routing."
  }
}

"parameters" "enableOmsAgent" {
  "type" = "bool"

  "defaultValue" = true

  "metadata" = {
    "description" = "Boolean flag to turn on and off of omsagent addon."
  }
}

"parameters" "workspaceRegion" {
  "type" = "string"

  "defaultValue" = "East US"

  "metadata" = {
    "description" = "Specify the region for your OMS workspace."
  }
}

"parameters" "workspaceName" {
  "type" = "string"

  "metadata" = {
    "description" = "Specify the name of the OMS workspace."
  }
}

"parameters" "omsWorkspaceId" {
  "type" = "string"

  "metadata" = {
    "description" = "Specify the resource id of the OMS workspace."
  }
}

"parameters" "omsSku" {
  "type" = "string"

  "defaultValue" = "standalone"

  "allowedValues" = ["free", "standalone", "pernode"]

  "metadata" = {
    "description" = "Select the SKU for your workspace."
  }
}

"parameters" "principalId" {
  "type" = "string"

  "metadata" = {
    "description" = "The objectId of service principal."
  }
}

"parameters" "vnetSubnetID" {
  "type" = "string"

  "metadata" = {
    "description" = "Resource ID of virtual network subnet used for nodes and/or pods IP assignment."
  }
}

"parameters" "serviceCidr" {
  "type" = "string"

  "metadata" = {
    "description" = "A CIDR notation IP range from which to assign service cluster IPs."
  }
}

"parameters" "dnsServiceIP" {
  "type" = "string"

  "metadata" = {
    "description" = "Containers DNS server IP address."
  }
}

"parameters" "dockerBridgeCidr" {
  "type" = "string"

  "metadata" = {
    "description" = "A CIDR notation IP for Docker bridge."
  }
}

"resources" = {
  "apiVersion" = "2019-08-01"

  "dependsOn" = ["[concat('Microsoft.Resources/deployments/', 'WorkspaceDeployment-20191210120359')]", "Microsoft.Network/virtualNetworks/manual-rg-vnet", "[concat('Microsoft.Resources/deployments/', 'ClusterSubnetRoleAssignmentDeployment-20191210120359')]"]

  "type" = "Microsoft.ContainerService/managedClusters"

  "location" = "[parameters('location')]"

  "name" = "[parameters('resourceName')]"

  "properties" = {
    "kubernetesVersion" = "[parameters('kubernetesVersion')]"

    "enableRBAC" = "[parameters('enableRBAC')]"

    "dnsPrefix" = "[parameters('dnsPrefix')]"

    "agentPoolProfiles" = {
      "name" = "agentpool"

      "osDiskSizeGB" = "[parameters('osDiskSizeGB')]"

      "count" = "[parameters('agentCount')]"

      "vmSize" = "[parameters('agentVMSize')]"

      "osType" = "[parameters('osType')]"

      "storageProfile" = "ManagedDisks"

      "type" = "VirtualMachineScaleSets"

      "vnetSubnetID" = "[parameters('vnetSubnetID')]"
    }

    "servicePrincipalProfile" = {
      "ClientId" = "[parameters('servicePrincipalClientId')]"

      "Secret" = "[parameters('servicePrincipalClientSecret')]"

      "aadSessionKey" = "[parameters('aadSessionKey')]"
    }

    "networkProfile" = {
      "loadBalancerSku" = "standard"

      "networkPlugin" = "[parameters('networkPlugin')]"

      "serviceCidr" = "[parameters('serviceCidr')]"

      "dnsServiceIP" = "[parameters('dnsServiceIP')]"

      "dockerBridgeCidr" = "[parameters('dockerBridgeCidr')]"
    }

    "addonProfiles" "httpApplicationRouting" {
      "enabled" = "[parameters('enableHttpApplicationRouting')]"
    }

    "addonProfiles" "omsagent" {
      "enabled" = "[parameters('enableOmsAgent')]"

      "config" = {
        "logAnalyticsWorkspaceResourceID" = "[parameters('omsWorkspaceId')]"
      }
    }
  }

  "tags" = {
    "manual" = "true"
  }
}

"resources" = {
  "type" = "Microsoft.Resources/deployments"

  "name" = "SolutionDeployment-20191210120359"

  "apiVersion" = "2017-05-10"

  "resourceGroup" = "[split(parameters('omsWorkspaceId'),'/')[4]]"

  "subscriptionId" = "[split(parameters('omsWorkspaceId'),'/')[2]]"

  "properties" = {
    "mode" = "Incremental"

    "template" = {
      "$schema" = "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"

      "contentVersion" = "1.0.0.0"

      "parameters" = {}

      "variables" = {}

      "resources" = {
        "apiVersion" = "2015-11-01-preview"

        "type" = "Microsoft.OperationsManagement/solutions"

        "location" = "[parameters('workspaceRegion')]"

        "name" = "[concat('ContainerInsights', '(', split(parameters('omsWorkspaceId'),'/')[8], ')')]"

        "properties" = {
          "workspaceResourceId" = "[parameters('omsWorkspaceId')]"
        }

        "plan" = {
          "name" = "[concat('ContainerInsights', '(', split(parameters('omsWorkspaceId'),'/')[8], ')')]"

          "product" = "[concat('OMSGallery/', 'ContainerInsights')]"

          "promotionCode" = ""

          "publisher" = "Microsoft"
        }
      }
    }
  }

  "dependsOn" = ["[concat('Microsoft.Resources/deployments/', 'WorkspaceDeployment-20191210120359')]"]
}

"resources" = {
  "type" = "Microsoft.Resources/deployments"

  "name" = "WorkspaceDeployment-20191210120359"

  "apiVersion" = "2017-05-10"

  "resourceGroup" = "[split(parameters('omsWorkspaceId'),'/')[4]]"

  "subscriptionId" = "[split(parameters('omsWorkspaceId'),'/')[2]]"

  "properties" = {
    "mode" = "Incremental"

    "template" = {
      "$schema" = "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"

      "contentVersion" = "1.0.0.0"

      "parameters" = {}

      "variables" = {}

      "resources" = {
        "apiVersion" = "2015-11-01-preview"

        "type" = "Microsoft.OperationalInsights/workspaces"

        "location" = "[parameters('workspaceRegion')]"

        "name" = "[parameters('workspaceName')]"

        "properties" "sku" {
          "name" = "[parameters('omsSku')]"
        }
      }
    }
  }
}

"resources" = {
  "type" = "Microsoft.Resources/deployments"

  "name" = "ClusterMonitoringMetricPulisherRoleAssignmentDepl-20191210120359"

  "apiVersion" = "2017-05-10"

  "resourceGroup" = "manual-rg"

  "subscriptionId" = "f66a2d2c-ddff-4567-9f0d-5ff84db7e238"

  "properties" = {
    "mode" = "Incremental"

    "template" = {
      "$schema" = "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"

      "contentVersion" = "1.0.0.0"

      "parameters" = {}

      "variables" = {}

      "resources" = {
        "type" = "Microsoft.ContainerService/managedClusters/providers/roleAssignments"

        "apiVersion" = "2018-01-01-preview"

        "name" = "manual-akl-cluster/Microsoft.Authorization/8a2240c4-88ad-4bb3-8a16-acdaf7f2694c"

        "properties" = {
          "roleDefinitionId" = "[concat('/subscriptions/', subscription().subscriptionId, '/providers/Microsoft.Authorization/roleDefinitions/', '3913510d-42f4-4e42-8a64-420c390055eb')]"

          "principalId" = "[parameters('principalId')]"

          "scope" = "/subscriptions/f66a2d2c-ddff-4567-9f0d-5ff84db7e238/resourceGroups/manual-rg/providers/Microsoft.ContainerService/managedClusters/manual-akl-cluster"
        }
      }
    }
  }

  "dependsOn" = ["/subscriptions/f66a2d2c-ddff-4567-9f0d-5ff84db7e238/resourceGroups/manual-rg/providers/Microsoft.ContainerService/managedClusters/manual-akl-cluster"]
}

"resources" = {
  "apiVersion" = "2019-04-01"

  "name" = "manual-rg-vnet"

  "type" = "Microsoft.Network/virtualNetworks"

  "location" = "eastus"

  "properties" = {
    "subnets" = {
      "name" = "default"

      "id" = "/subscriptions/f66a2d2c-ddff-4567-9f0d-5ff84db7e238/resourceGroups/manual-rg/providers/Microsoft.Network/virtualNetworks/manual-rg-vnet/subnets/default"

      "properties" = {
        "addressPrefix" = "10.240.0.0/16"
      }
    }

    "addressSpace" = {
      "addressPrefixes" = ["10.0.0.0/8"]
    }
  }

  "tags" = {}
}

"resources" = {
  "type" = "Microsoft.Resources/deployments"

  "name" = "ClusterSubnetRoleAssignmentDeployment-20191210120359"

  "apiVersion" = "2017-05-10"

  "resourceGroup" = "manual-rg"

  "subscriptionId" = "f66a2d2c-ddff-4567-9f0d-5ff84db7e238"

  "properties" = {
    "mode" = "Incremental"

    "template" = {
      "$schema" = "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"

      "contentVersion" = "1.0.0.0"

      "parameters" = {}

      "variables" = {}

      "resources" = {
        "type" = "Microsoft.Network/virtualNetworks/subnets/providers/roleAssignments"

        "apiVersion" = "2017-05-01"

        "name" = "manual-rg-vnet/default/Microsoft.Authorization/fcd9031f-1ff6-4710-b12d-49725f66ff7a"

        "properties" = {
          "roleDefinitionId" = "[concat('/subscriptions/', subscription().subscriptionId, '/providers/Microsoft.Authorization/roleDefinitions/', '4d97b98b-1d4f-4787-a291-c67834d212e7')]"

          "principalId" = "[parameters('principalId')]"

          "scope" = "/subscriptions/f66a2d2c-ddff-4567-9f0d-5ff84db7e238/resourceGroups/manual-rg/providers/Microsoft.Network/virtualNetworks/manual-rg-vnet/subnets/default"
        }
      }
    }
  }

  "dependsOn" = ["Microsoft.Network/virtualNetworks/manual-rg-vnet"]
}

"outputs" "controlPlaneFQDN" {
  "type" = "string"

  "value" = "[reference(concat('Microsoft.ContainerService/managedClusters/', parameters('resourceName'))).fqdn]"
}

