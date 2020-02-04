import unittest
from myazure.aks import AksClient
from unittest.mock import MagicMock, patch
import os
from pytest_dotenv import plugin


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_e2e(self):
        plugin.load_dotenv()
        client = AksClient()
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
        try:
            status = client.create(config)
        except Exception as e:
            print(e.args[0])
        self.assertEqual(status, "Succeeded")


if __name__ == '__main__':
    unittest.main()
