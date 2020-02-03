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

    def create(self, config):
        client_id = os.environ.get("AZURE_CLIENT_ID", None)
        secret = os.environ.get("AZURE_CLIENT_SECRET", None)
        # asyncCreate = self.cs_client.container_services.create_or_update(
        #     config['resource_group'],
        #     config['container_name'],
        #     {
        #         'location': config['location'],
        #         "orchestrator_profile": {
        #             "orchestrator_type": "Kubernetes"
        #         },
        #         "master_profile": {
        #             "count": 1,
        #             "dns_prefix": "MasterPrefixTest",
        #             "vm_size": "Standard_D2s_v3"
        #         },
        #         "agent_pool_profiles": [{
        #             "name": "agentpool0",
        #             "count": 3,
        #             "vm_size": "Standard_D2s_v3",
        #             "dns_prefix": "AgentPrefixTest"  # - Optional in latest version
        #         }],
        #         "linux_profile": {
        #             "admin_username": "acslinuxadmin",
        #             "ssh": {
        #                 "public_keys": [{
        #                     "key_data": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDWM58od7yvDBt+FYBr1ZPKIwKv50KR7SDDPA4nDqfxdLSwa1dDgHPnI0MuqJqJ1AECtgXHy+EbMf6yUJwPe8T3EZlNT43880FJfbcgalvP3AyxCmR332Oya1XW/8FtXB0+5vH//V0RdXV3NwWIkTfB8Ndkk6dEL8dXpaYqhoa8vam6mtLejxZ/qy19Cc0xgi0a5S2b4VJ3R4NNQuLsIqnLIxgHshAya9l9HejKbQXxReFlJgMHt/BcDiOjv8rPr98KDm5viKaT9v2ws+cAF/x3fnOvd8R41e5I7GaJfKhNtm4Dc0QJ7ip8l2DpJlyveeFqX0an69W7Ty3lvFulUIYz pramodjangam@Pramods-MacBook-Pro.local"
        #                 }]
        #             }
        #         },
        #         "servicePrincipalProfile": {
        #             "secret": secret,
        #             "clientId": client_id
        #         }
        #     }
        # )

        asyncCreate = self.cs_client.managed_clusters.create_or_update(
            config['resource_group'],
            config['container_name'],
            {
                "location": config['location'],
                # "tags": {
                #     "tier": "production",
                #     "archv2": ""
                # },
                "properties": {
                    # "kubernetesVersion": "",
                    "dnsPrefix": "dnsprefix1",
                    "agentPoolProfiles": [
                        {
                            "name": "nodepool1",
                            "count": 3,
                            "vmSize": "Standard_D2s_v3",
                            "osType": "Linux",
                            "type": "VirtualMachineScaleSets",
                            "availabilityZones": [
                                "1",
                                "2",
                                "3"
                            ],
                            "enableNodePublicIP": False
                        }
                    ],
                    "linuxProfile": {
                        "adminUsername": "azureuser",
                        "ssh": {
                            "publicKeys": [
                                {
                                    "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDWM58od7yvDBt+FYBr1ZPKIwKv50KR7SDDPA4nDqfxdLSwa1dDgHPnI0MuqJqJ1AECtgXHy+EbMf6yUJwPe8T3EZlNT43880FJfbcgalvP3AyxCmR332Oya1XW/8FtXB0+5vH//V0RdXV3NwWIkTfB8Ndkk6dEL8dXpaYqhoa8vam6mtLejxZ/qy19Cc0xgi0a5S2b4VJ3R4NNQuLsIqnLIxgHshAya9l9HejKbQXxReFlJgMHt/BcDiOjv8rPr98KDm5viKaT9v2ws+cAF/x3fnOvd8R41e5I7GaJfKhNtm4Dc0QJ7ip8l2DpJlyveeFqX0an69W7Ty3lvFulUIYz pramodjangam@Pramods-MacBook-Pro.local"
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
        )
        container = asyncCreate.result()
        print(container)
        return container.provisioning_state

    def create_mgmt_client(self, client_class, **kwargs):
        subscription_id = None
        # if self.is_live:
        subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", None)
        # if not subscription_id:
        #    subscription_id = self.settings.SUBSCRIPTION_ID

        return self.create_basic_client(
            client_class,
            subscription_id=subscription_id,
            **kwargs
        )

    def create_basic_client(self, client_class, **kwargs):
        tenant_id = os.environ.get("AZURE_TENANT_ID", None)
        client_id = os.environ.get("AZURE_CLIENT_ID", None)
        secret = os.environ.get("AZURE_CLIENT_SECRET", None)

        if tenant_id and client_id and secret and self.is_live:
            from msrestazure.azure_active_directory import ServicePrincipalCredentials
            credentials = ServicePrincipalCredentials(
                tenant=tenant_id,
                client_id=client_id,
                secret=secret
            )
        else:
            credentials = self.settings.get_credentials()
        subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", None)
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
