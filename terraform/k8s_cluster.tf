resource "azurerm_kubernetes_cluster" "hello_cluster" {
  dns_prefix = "hello"
  location = azurerm_resource_group.rg_main.location
  name = "hello"
  resource_group_name = azurerm_resource_group.rg_main.name
  count = 1
  agent_pool_profile {
    name = "dfagentpool"
    vm_size = var.agentVMSize
    count = 1
  }

  service_principal {
    client_secret var.client_secret
    client_id = var.client_id
  }
}

output "client_certificate" {
  value = azurerm_kubernetes_cluster.hello_cluster.0.kube_config.0.client_certificate
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.hello_cluster.0.kube_config_raw
}

