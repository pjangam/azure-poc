resource "azurerm_kubernetes_cluster" "hello_cluster" {
  dns_prefix = "hello"
  location = azurerm_resource_group.rg_main.location
  name = "hello"
  resource_group_name = azurerm_resource_group.rg_main.name
  count = 1
  default_node_pool {
    name = "dfagentpool"
    vm_size = var.agentVMSize
    node_count = 1
    availability_zones = []
    enable_auto_scaling = false
    enable_node_public_ip = false
    node_taints = []
    os_disk_size_gb = 100
    type = "AvailabilitySet"
  }
  role_based_access_control {
    enabled = false

  }
  service_principal {
    client_secret = var.client_secret
    client_id = var.client_id
  }
  api_server_authorized_ip_ranges : []
}

output "client_certificate" {
  value = azurerm_kubernetes_cluster.hello_cluster.0.kube_config.0.client_certificate
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.hello_cluster.0.kube_config_raw
}

