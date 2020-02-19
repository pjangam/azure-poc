import os
import azure.mgmt.containerservice
import msrestazure.azure_active_directory
from msrestazure.azure_exceptions import CloudError

from myazure.aks_config import AksConfig


def get_env(env_name):
    val: str = os.environ.get(env_name)
    if not val:
        raise EnvironmentError(f'{env_name} is not set.')
    if val.startswith('"') and val.endswith('"'):
        val = val[1:-1]
    return val


def get_network_profile():
    return {
        "loadBalancerSku": "standard",
        "networkPlugin": "kubenet",  # or azure

        # "outboundType": "loadBalancer",
        "loadBalancerProfile": {
            "managedOutboundIPs": {
                "count": 1
            }
        }
    }


def get_linux_profile(public_key):
    return {
        "adminUsername": "azureuser",
        "ssh": {
            "publicKeys": [
                {
                    "keyData": public_key
                }
            ]
        }
    }


def get_agent_profiles(agent_pools):
    result = []
    for agent_pool in agent_pools:
        result.append({
            "name": agent_pool.profile_name,
            "osDiskSizeGB": 100,
            "maxPods": 30,
            "count": agent_pool.node_count,
            "vmSize": agent_pool.size,
            "osType": agent_pool.os_type,
            "storageProfile": "ManagedDisks",
            "type": "VirtualMachineScaleSets"

            # "availabilityZones": agent_pool.availability_zones
            # "enableNodePublicIP": False,
            # "vnetSubnetID": "[parameters('vnetSubnetID')]"
        })

    return result


class AksClient:
    def __init__(self):
        self.test_mode = 'None'.lower()
        self.subscription_id = get_env("AZURE_SUBSCRIPTION_ID")
        self.client_id = get_env("AZURE_CLIENT_ID")
        self.secret = get_env("AZURE_CLIENT_SECRET")
        self.tenant_id = get_env("AZURE_TENANT_ID")
        self.public_key = get_env("PUBLIC_KEY")

        cs_client1 = self.__create_mgmt_client(
            azure.mgmt.containerservice.ContainerServiceClient
        )
        self.cs_client = cs_client1

    def create(self, config: AksConfig):
        config_azure_format = self.__get_config(config)

        async_create = self.cs_client.managed_clusters.create_or_update(
            config.resource_group,
            config.cluster_name,
            config_azure_format
        )
        # wait for creation succeed
        # TODO: try to get polling status to console/ response
        container = async_create.result()
        return container.provisioning_state

    def get(self, resource_group, cluster_name):
        cluster = self.cs_client.managed_clusters.get(resource_group, cluster_name)
        if cluster is not None:
            print(cluster)
            return cluster.name
        else:
            return "Failed"

    def update(self, config: AksConfig):
        # make sure cluster exists

        config_azure_format = self.__get_config(config)

        async_create = self.cs_client.managed_clusters.update(
            config.resource_group,
            config.cluster_name,
            config_azure_format
        )
        # wait for creation succeed
        # TODO: try to get polling status to console/ response
        container = async_create.result()
        return container.provisioning_state
        pass

    def delete(self, resource_group, cluster_name):
        async_action = self.cs_client.managed_clusters.delete(resource_group, cluster_name)
        async_action.result()
        return "Succeeded"

    # private
    def __create_mgmt_client(self, client_class, **kwargs):
        return self.__create_basic_client(
            client_class,
            subscription_id=self.subscription_id,
            **kwargs
        )

    # noinspection PyUnusedLocal
    def __create_basic_client(self, client_class, **kwargs):
        credentials = msrestazure.azure_active_directory.ServicePrincipalCredentials(
            tenant=self.tenant_id,
            client_id=self.client_id,
            secret=self.secret
        )
        # Real client creation
        subscription_id = self.subscription_id
        client = client_class(
            credentials=credentials,
            subscription_id=subscription_id
            # **kwargs
        )
        client.config.enable_http_logger = True
        return client

    def __get_config(self, config: AksConfig):
        return {
            "location": config.location,
            "tags": config.tags,
            "properties": self.__get_properties(config)
        }

    def __get_properties(self, config):
        return {
            # "kubernetesVersion": "",
            "dnsPrefix": config.dns_prefix,
            "agentPoolProfiles": get_agent_profiles(config.agent_pools),
            # "nodeResourceGroup":"firstapp-resources",
            # "linuxProfile": get_linux_profile(self.public_key),
            "networkProfile": get_network_profile(),

            "servicePrincipalProfile": self.__get_service_principle(),
            "addonProfiles": {
            },
            "enableRBAC": True,
            "diskEncryptionSetID": "/subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.Compute"
                                   "/diskEncryptionSets/des",
            "enablePodSecurityPolicy": False
        }

    def __get_service_principle(self):
        return {
            "clientId": self.client_id,
            "secret": self.secret
        }
