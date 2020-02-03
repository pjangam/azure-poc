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
        self.cs_client.container_services.create_or_update(
            config['resource_group'],
            config['container_name'],
            {
                'location': config['location'],
                "orchestrator_profile": {
                    "orchestrator_type": "DCOS"
                },
                "master_profile": {
                    "count": 1,
                    "dns_prefix": "MasterPrefixTest",
                    "vm_size": "standard_d2_v2"
                },
                "agent_pool_profiles": [{
                    "name": "agentpool0",
                    "count": 3,
                    "vm_size": "Standard_A2_v2",
                    # "dns_prefix": "AgentPrefixTest" - Optional in latest version
                }],
                "linux_profile": {
                    "admin_username": "acslinuxadmin",
                    "ssh": {
                        "public_keys": [{
                            "key_data": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAlj9UC6+57XWVu0fd6zqXa256EU9EZdoLGE3TqdZqu9fvUvLQOX2G0d5DmFhDCyTmWLQUx3/ONQ9RotYmHGymBIPQcpx43nnxsuihAILcpGZ5NjCj4IOYnmhdULxN4ti7k00S+udqokrRYpmwt0N4NA4VT9cN+7uJDL8Opqa1FYu0CT/RqSW+3aoQ0nfGj11axoxM37FuOMZ/c7mBSxvuI9NsDmcDQOUmPXjlgNlxrLzf6VcjxnJh4AO83zbyLok37mW/C7CuNK4WowjPO1Ix2kqRHRxBrzxYZ9xqZPc8GpFTw/dxJEYdJ3xlitbOoBoDgrL5gSITv6ESlNqjPk6kHQ== azureuser@linuxvm"
                        }]
                    }
                },
            },
        )
        print("hi")
        return "bye"

    def create_mgmt_client(self, client_class, **kwargs):
        subscription_id = None
        #if self.is_live:
        subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", None)
        #if not subscription_id:
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
