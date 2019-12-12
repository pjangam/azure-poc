terraform {
  required_version = "0.12.17"
   backend "azurerm" {
          storage_account_name = "eepoctfstate"
          container_name       = "tfstate"
          key                  = "firstapp.terraform.tfstate"
          resource_group_name  = "akspochelloworldabc5-rg"
      }
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