from pkg_resources import resource_dir

import environs
import unittest
import web3
import os
from web3.contract import Contract
from snet.contracts.utils import *


mainnet_endpoint = os.environ.get("MAINNET_ENDPOINT")
sepolia_endpoint = os.environ.get("SEPOLIA_ENDPOINT")

w3_mainnet = web3.Web3(web3.HTTPProvider(mainnet_endpoint))
w3_sepolia = web3.Web3(web3.HTTPProvider(sepolia_endpoint))

contract_names = ["MultiPartyEscrow", "Registry", "SingularityNetToken", "TokenConversionManager",
                  "TokenStake", "TokenConversionManagerV2", "TokenConversionManagerV3"]


class TestGetContractDefOnlyAbi(unittest.TestCase):
    def test_mpe(self):
        name = "MultiPartyEscrow"
        contract_def = get_contract_def(name)
        self.assertEqual("abi" in contract_def, True)

    def test_registry(self):
        name = "Registry"
        contract_def = get_contract_def(name)
        self.assertEqual("abi" in contract_def, True)

    def test_snt(self):
        name = "SingularityNetToken"
        contract_def = get_contract_def(name)
        self.assertEqual("abi" in contract_def, True)

    def test_tcm(self):
        name = "TokenConversionManager"
        contract_def = get_contract_def(name)
        self.assertEqual("abi" in contract_def, True)

    def test_tst(self):
        name = "TokenStake"
        contract_def = get_contract_def(name)
        self.assertEqual("abi" in contract_def, True)

    def test_tcm2(self):
        name = "TokenConversionManagerV2"
        contract_def = get_contract_def(name)
        self.assertEqual("abi" in contract_def, True)

    def test_tcm3(self):
        name = "TokenConversionManagerV3"
        contract_def = get_contract_def(name)
        self.assertEqual("abi" in contract_def, True)


class TestGetContractDefNetworks(unittest.TestCase):
    def test_mpe(self):
        name = "MultiPartyEscrow"
        contract_def = get_contract_def(name)
        self.assertEqual("networks" in contract_def, True)

    def test_registry(self):
        name = "Registry"
        contract_def = get_contract_def(name)
        self.assertEqual("networks" in contract_def, True)

    def test_snt(self):
        name = "SingularityNetToken"
        contract_def = get_contract_def(name)
        self.assertEqual("networks" in contract_def, True)

    # def test_tcm(self):
    #     name = "TokenConversionManager"
    #     contract_def = get_contract_def(name)
    #     self.assertEqual("networks" in contract_def, True)

    def test_tst(self):
        name = "TokenStake"
        contract_def = get_contract_def(name)
        self.assertEqual("networks" in contract_def, True)

    # def test_tcm2(self):
    #     name = "TokenConversionManagerV2"
    #     contract_def = get_contract_def(name)
    #     self.assertEqual("networks" in contract_def, True)
    #
    # def test_tcm3(self):
    #     name = "TokenConversionManagerV3"
    #     contract_def = get_contract_def(name)
    #     self.assertEqual("networks" in contract_def, True)


class TestGetContractDefNegative(unittest.TestCase):
    def test_negative_name(self):
        name = "abcdefghijklmn"
        with self.assertRaises(FileNotFoundError):
            contract_def = get_contract_def(name)

    def test_negative_root(self):
        name = "MultiPartyEscrow"
        resources_path = os.path.curdir
        with self.assertRaises(FileNotFoundError):
            contract_def = get_contract_def(name, resources_path)

if __name__ == '__main__':
    unittest.main()
