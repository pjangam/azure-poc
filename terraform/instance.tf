resource "azurerm_virtual_machine" "api_server" {
  location = "${azurerm_resource_group.rg_main.location}"
  name = "api_server"
  network_interface_ids = ["${azurerm_network_interface.main.id}"]
  resource_group_name   = "${azurerm_resource_group.rg_main.name}"
  vm_size = "Standard_DS1_v2"

  storage_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
  storage_os_disk {
    name              = "myosdisk1"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }
  os_profile {
    admin_username = "pjangam"
    computer_name = "xero"
    admin_password = "1qaz!QAZ"
  }
  os_profile_linux_config {
    disable_password_authentication = false
  }

}

