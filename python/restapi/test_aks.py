import unittest
from unittest import mock
from unittest.mock import patch
from pytest_dotenv import plugin

from myazure.aks import AksClient, AksConfig


def get_mock_enviorn():
    return {'AZURE_CLIENT_ID': 'xyz',
            'AZURE_CLIENT_SECRET': 'xyz',
            'AZURE_TENANT_ID': 'xyz',
            'AZURE_SUBSCRIPTION_ID': 'xyz',
            'PUBLIC_KEY': "xyz"}


def get_request_config_dict():
    config = {
        "resource_group": "firstapp-resources",
        "cluster_name": "test-python-container-pj2",
        "location": "West US 2",
        "dns_prefix": "dnsPrefix",
        "node_count": 2,
        "size": "Standard_D2s_v3"
    }
    return config


def to_obj(aks_client_result):
    aks_client_result_obj = type('', (object,), aks_client_result)()
    return aks_client_result_obj


def get_request_config():
    config = get_request_config_dict()
    aks_config = AksConfig(config)
    return aks_config


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        # mock.patch.dict('os.environ', get_mock_enviorn())
        plugin.load_dotenv()

    # def test_e2e(self):
    #     plugin.load_dotenv()
    #     client = AksClient()
    #     config = {
    #         "resource_group": "firstapp-resources",
    #         "cluster_name": "test-python-container-pj2",
    #         "location": "West US 2",
    #         "dns_prefix": "dnsPrefix",
    #         "node_count": 2,
    #         "size": "Standard_D2s_v3",
    #         "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDWM58od7yvDBt"
    #                       "+FYBr1ZPKIwKv50KR7SDDPA4nDqfxdLSwa1dDgHPnI0MuqJqJ1AECtgXHy"
    #                       "+EbMf6yUJwPe8T3EZlNT43880FJfbcgalvP3AyxCmR332Oya1XW/8FtXB0+5vH"
    #                       "//V0RdXV3NwWIkTfB8Ndkk6dEL8dXpaYqhoa8vam6mtLejxZ"
    #                       "/qy19Cc0xgi0a5S2b4VJ3R4NNQuLsIqnLIxgHshAya9l9HejKbQXxReFlJgMHt/BcDiOjv8rPr98KDm5viKaT9v2ws"
    #                       "+cAF/x3fnOvd8R41e5I7GaJfKhNtm4Dc0QJ7ip8l2DpJlyveeFqX0an69W7Ty3lvFulUIYz "
    #                       "pramodjangam@Pramods-MacBook-Pro.local "
    #     }
    #     try:
    #         status = client.create(config)
    #     except Exception as e:
    #         print(e.args[0])
    #     self.assertEqual(status, "Succeeded")

    def test_parse_config(self):
        config = get_request_config_dict()
        aks_config = AksConfig(config)
        self.assertEqual(config['resource_group'], aks_config.resource_group)
        for keys in config.keys():
            self.assertTrue(hasattr(aks_config, keys), f'{keys} not present in object"')
            self.assertEqual(getattr(aks_config, keys), config[keys])
        for attr in dir(aks_config):
            if not attr.startswith('__') and attr != 'tags':
                self.assertIsNotNone(getattr(aks_config, attr), f'{attr} is none but expected to have some value')

    @patch('azure.mgmt.containerservice.ContainerServiceClient')
    @patch('msrestazure.azure_active_directory.ServicePrincipalCredentials')
    def test_givenAksCreateReturnsSucceeded_whenUserCallCreate_thenStatusSuccessReturned(
            self, mock_service_principle, mock_aks_client
    ):
        # with mock.patch.dict('os.environ', get_mock_enviorn()):
        print(mock_service_principle)

        # Given

        mock_aks_client.return_value \
            .managed_clusters \
            .create_or_update.return_value \
            .result.return_value = to_obj({"provisioning_state": "Succeeded"})
        aks_config = get_request_config()
        aks_client = AksClient()
        # When
        status = aks_client.create(aks_config)
        # Then
        self.assertEqual("Succeeded", status)


if __name__ == '__main__':
    unittest.main()
