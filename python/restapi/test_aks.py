import unittest
from myazure.aks import AksClient, AksConfig
from unittest.mock import MagicMock, patch
import os
from pytest_dotenv import plugin


class TestStringMethods(unittest.TestCase):

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
        config = {
            "resource_group": "firstapp-resources",
            "cluster_name": "test-python-container-pj2",
            "location": "West US 2",
            "dns_prefix": "dnsPrefix",
            "node_count": 2,
            "size": "Standard_D2s_v3",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDWM58od7yvDBt"
                          "+FYBr1ZPKIwKv50KR7SDDPA4nDqfxdLSwa1dDgHPnI0MuqJqJ1AECtgXHy"
                          "+EbMf6yUJwPe8T3EZlNT43880FJfbcgalvP3AyxCmR332Oya1XW/8FtXB0+5vH"
                          "//V0RdXV3NwWIkTfB8Ndkk6dEL8dXpaYqhoa8vam6mtLejxZ"
                          "/qy19Cc0xgi0a5S2b4VJ3R4NNQuLsIqnLIxgHshAya9l9HejKbQXxReFlJgMHt/BcDiOjv8rPr98KDm5viKaT9v2ws"
                          "+cAF/x3fnOvd8R41e5I7GaJfKhNtm4Dc0QJ7ip8l2DpJlyveeFqX0an69W7Ty3lvFulUIYz "
                          "pramodjangam@Pramods-MacBook-Pro.local "
        }
        aks_config = AksConfig(config)
        self.assertEqual(config['resource_group'], aks_config.resource_group)
        for keys in config.keys():
            self.assertTrue(hasattr(aks_config, keys), f'{keys} not present in object"')
            self.assertEqual(getattr(aks_config, keys), config[keys])
        for attr in dir(aks_config):
            if not attr.startswith('__'):
                self.assertIsNotNone(getattr(aks_config,attr))


if __name__ == '__main__':
    unittest.main()
