import os
import azure.mgmt.containerservice


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
        "outboundType": "loadBalancer",
        "loadBalancerProfile": {
            "managedOutboundIPs": {
                "count": 2
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


def get_agent_profiles(node_count, vm_size, os_type, availability_zones):
    return [
        # todo:support multiple node pools with different config
        {
            "name": "dfagentpool",
            "count": node_count,
            "vmSize": vm_size,
            "osType": os_type,
            "type": "VirtualMachineScaleSets",
            "availabilityZones": availability_zones,
            "enableNodePublicIP": False
        }
    ]


class AksClient:
    def __init__(self):
        self.test_mode = 'None'.lower()
        self.subscription_id = get_env("AZURE_SUBSCRIPTION_ID")
        self.client_id = get_env("AZURE_CLIENT_ID")
        self.secret = get_env("AZURE_CLIENT_SECRET")
        self.tenant_id = get_env("AZURE_TENANT_ID")

        self.cs_client = self.create_mgmt_client(
            azure.mgmt.containerservice.ContainerServiceClient
        )

    def is_playback(self):
        return self.test_mode == "playback"

    def create(self, config):
        resource_group = config['resource_group']
        cluster_name = config['cluster_name']
        location = config['location']
        dns_prefix = config['dns_prefix']
        node_count: int = config['node_count']
        vm_size = config["size"]
        os_type = 'Linux'
        last_num = min(3, node_count) + 1
        availability_zones = list(map(lambda x: str(x), range(1, last_num)))
        if "os" in config:
            os_type = config["os"]
        tags = None
        if 'tags' in config:
            tags = config['tags']

        public_key = config["public_key"]

        config1 = self.get_config(location, dns_prefix,
                                  node_count, vm_size, os_type, availability_zones, public_key, tags)

        async_create = self.cs_client.managed_clusters.create_or_update(
            resource_group,
            cluster_name,
            config1
        )
        container = async_create.result()
        print(container)
        return container.provisioning_state

    def create_mgmt_client(self, client_class, tags=None, **kwargs):
        return self.create_basic_client(
            client_class,
            tags,
            subscription_id=self.subscription_id,
            **kwargs
        )

    # noinspection PyUnusedLocal
    def create_basic_client(self, client_class, tags=None, **kwargs):

        from msrestazure.azure_active_directory import ServicePrincipalCredentials
        credentials = ServicePrincipalCredentials(
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
        if self.is_playback():
            client.config.long_running_operation_timeout = 0
        client.config.enable_http_logger = True
        return client

    def get_config(self, location, dns_prefix, node_count, vm_size, os_type, availability_zones, public_key, tags):
        return {
            "location": location,
            "tags": tags,
            "properties": self.get_properties(dns_prefix, node_count, vm_size, os_type, availability_zones, public_key)
        }

    def get_properties(self, dns_prefix, node_count, vm_size, os_type, availability_zones, public_key):
        return {
            # "kubernetesVersion": "",
            "dnsPrefix": dns_prefix,
            "agentPoolProfiles": get_agent_profiles(node_count, vm_size, os_type, availability_zones),
            "linuxProfile": get_linux_profile(public_key),
            "networkProfile": get_network_profile(),

            "servicePrincipalProfile": self.get_service_principle(),
            "addonProfiles": {},
            "enableRBAC": True,
            "diskEncryptionSetID": "/subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.Compute"
                                   "/diskEncryptionSets/des",
            "enablePodSecurityPolicy": False
        }

    def get_service_principle(self):
        return {
            "clientId": self.client_id,
            "secret": self.secret
        }
