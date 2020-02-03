from azureml.core.compute import AksCompute, ComputeTarget
from azureml.core import Workspace
import os
import azurerm


def create(data):
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", None)
    token = azurerm.get_access_token_from_cli()
    resource_groups = azurerm.list_resource_groups(token, subscription_id)
    for rg in resource_groups['value']:
        print(rg["name"] + ', ' + rg['location'] + ', ' + rg['properties']['provisioningState'])
    

    # Uses the specific FPGA enabled VM (sku: Standard_PB6s)
    # Standard_PB6s are available in: eastus, westus2, westeurope, southeastasia
    prov_config = AksCompute.provisioning_configuration(vm_size="Standard_PB6s",
                                                        agent_count=1,
                                                        location="eastus")

    aks_name = 'my-aks-pb6'
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", None)
    workspace_name = 'DefaultWorkspace-136f4268-7dd0-446b-ab31-ec197ff147d5-WUS2'
    ws = Workspace(subscription_id, data['resource_group'], workspace_name, auth=None,
                   _location=None, _disable_service_check=False, _workspace_id=None, sku='basic')
    # Create the cluster
    aks_target = ComputeTarget.create(workspace=ws,
                                      name=aks_name,
                                      provisioning_configuration=prov_config)
    return "Hello"
