terraform {
  required_version = "0.12.17"
  //    backend "azurerm" {
  //        resource_group_name  = "StorageAccount-ResourceGroup"
  //        storage_account_name = "abcd1234"
  //        container_name       = "tfstate"
  //        key                  = "prod.terraform.tfstate"
  //    }
}

provider "azurerm" {
  //  client_id = ""
  //  client_secret = ""
}


resource "azurerm_resource_group" "rg_main" {
  name     = "firstapp-resources"
  location = "West US 2"
  //Southeast Asia
}