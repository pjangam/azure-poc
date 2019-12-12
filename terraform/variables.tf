variable "prefix" {
  default = "firstapp"
}
variable "ssh_key_path" {
  type = string
}
variable "agentVMSize" {
  default = "Standard_D2_v2"
}
variable "client_secret" {
  default = ""
}
variable "client_id" {
  default = ""
}