from azure.mgmt.containerservice import ContainerServiceClient
from azure.mgmt.deploymentmanager.operations import ArtifactSourcesOperations
import azure.mgmt.containerservice
import os


class get_aks:
    def __init__(self, credentials, subscriptionId):
        self.test_mode = 'None'.lower()
        self.cs_client = self.create_mgmt_client(
            azure.mgmt.containerservice.ContainerServiceClient
        )

    def is_playback(self):
        return self.test_mode == "playback"

    def get_env(self, envName, default):
        val = os.environ.get(envName, default)
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        return val

    def create(self, config):
        client_id = self.get_env("AZURE_CLIENT_ID", None)
        secret = self.get_env("AZURE_CLIENT_SECRET", None)

        resourceGroup = config['resource_group']
        clusterName = config['cluster_name']
        location = config['location']
        dnsPrefix = config['dns_prefix']
        nodeCount = config['node_count']
        vmSize = config["size"]
        osType = 'Linux'
        if "os" in config:
            osType = config["os"]
        lastNum = min(3, nodeCount) + 1
        availabilityZones = list(map(lambda x: str(x), range(1, lastNum)))

        publicKey = config["public_key"]

        config1 = self.get_config(resourceGroup, clusterName, location, dnsPrefix,
                                  nodeCount, vmSize, osType, availabilityZones, publicKey, client_id, secret)

        asyncCreate = self.cs_client.managed_clusters.create_or_update(
            resourceGroup,
            clusterName,
            config1
        )
        container = asyncCreate.result()
        print(container)
        return container.provisioning_state

    def create_mgmt_client(self, client_class, **kwargs):
        subscription_id = None
        # if self.is_live:
        subscription_id = self.get_env("AZURE_SUBSCRIPTION_ID", None)
        # if not subscription_id:
        #    subscription_id = self.settings.SUBSCRIPTION_ID

        return self.create_basic_client(
            client_class,
            subscription_id=subscription_id,
            **kwargs
        )

    def create_basic_client(self, client_class, **kwargs):
        tenant_id = self.get_env("AZURE_TENANT_ID", None)
        client_id = self.get_env("AZURE_CLIENT_ID", None)
        secret = self.get_env("AZURE_CLIENT_SECRET", None)

        print(client_id, tenant_id, secret)
        if tenant_id and client_id and secret and self.is_live:
            from msrestazure.azure_active_directory import ServicePrincipalCredentials
            credentials = ServicePrincipalCredentials(
                tenant=tenant_id,
                client_id=client_id,
                secret=secret
            )
        else:
            credentials = self.settings.get_credentials()
        subscription_id = self.get_env("AZURE_SUBSCRIPTION_ID", None)
        # Real client creation
        client = client_class(
            credentials=credentials,
            subscription_id=subscription_id
            # **kwargs
        )
        if self.is_playback():
            client.config.long_running_operation_timeout = 0
        client.config.enable_http_logger = True
        return client

    def is_live():
        """A module version of is_live, that could be used in pytest marker.
        """
        if not hasattr(is_live, '_cache'):
            config_file = os.path.join(
                os.path.dirname(__file__), TEST_SETTING_FILENAME)
            if not os.path.exists(config_file):
                config_file = None
            is_live._cache = TestConfig(config_file=config_file).record_mode
        return is_live._cache

    def get_config(self, resourceGroup, clusterName, location, dnsPrefix, nodeCount, vmSize, osType, availabilityZones, publicKey, client_id, secret):
        return {
            "location": location,
            # "tags": {
            #     "tier": "production",
            #     "archv2": ""
            # },
            "properties": {
                # "kubernetesVersion": "",
                "dnsPrefix": dnsPrefix,
                "agentPoolProfiles": [
                    # todo:support multiple node pools with different config
                    {
                        "name": "nodepool1",
                                "count": nodeCount,
                                "vmSize": vmSize,
                                "osType": osType,
                                "type": "VirtualMachineScaleSets",
                                "availabilityZones": availabilityZones,
                                "enableNodePublicIP": False
                    }
                ],
                "linuxProfile": {
                    "adminUsername": "azureuser",
                    "ssh": {
                        "publicKeys": [
                            {
                                "keyData": publicKey
                            }
                        ]
                    }
                },
                "networkProfile": {
                    "loadBalancerSku": "standard",
                    "outboundType": "loadBalancer",
                    "loadBalancerProfile": {
                        "managedOutboundIPs": {
                                    "count": 2
                        }
                    }
                },

                "servicePrincipalProfile": {
                    "clientId": client_id,
                    "secret": secret
                },
                "addonProfiles": {},
                "enableRBAC": True,
                "diskEncryptionSetID": "/subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.Compute/diskEncryptionSets/des",
                "enablePodSecurityPolicy": False
            }
        }
