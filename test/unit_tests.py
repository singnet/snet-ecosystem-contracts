import unittest
import web3
import os
from unittest import mock
from web3.contract import Contract
from snet.contracts.utils import *

mainnet_endpoint = os.environ.get("MAINNET_ENDPOINT")
sepolia_endpoint = os.environ.get("SEPOLIA_ENDPOINT")

w3_mainnet = web3.Web3(web3.HTTPProvider(mainnet_endpoint))
w3_sepolia = web3.Web3(web3.HTTPProvider(sepolia_endpoint))

contract_names = ["MultiPartyEscrow", "Registry", "SingularityNetToken", "TokenConversionManager",
                  "TokenStake", "TokenConversionManagerV2", "TokenConversionManagerV3", "FetchToken"]


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

    def test_tst(self):
        name = "TokenStake"
        contract_def = get_contract_def(name)
        self.assertEqual("networks" in contract_def, True)


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


class TestGetConverterAbi(unittest.TestCase):
    def test_agix_sepolia_v3(self):
        abi = get_converter_abi(11155111, "AGIX", "0xfdcDAE14927e8fA6b7490Ea855E888a7C957A880")
        self.assertEqual(abi, get_contract_def("TokenConversionManagerV3")["abi"])
        self.assertNotEqual(abi, get_contract_def("TokenConversionManager")["abi"])

    def test_ntx_sepolia_v3(self):
        abi = get_converter_abi("11155111", "NTX", "0xA21784B2Cb386EA6D67DfDaACee5a1a22977c8FC")
        self.assertEqual(abi, get_contract_def("TokenConversionManagerV3")["abi"])
        self.assertNotEqual(abi, get_contract_def("TokenConversionManager")["abi"])

    def test_cgv_mainnet(self):
        abi = get_converter_abi(1, "CGV", "0x698573504b1f44daADb2De17A3f6a11F2D005a79")
        self.assertEqual(abi, get_contract_def("TokenConversionManager")["abi"])

    def test_wmtx_mainnet(self):
        abi = get_converter_abi(1, "WMTX", "0x63BBC71C034bC99A905d5594dF985C218a35d392")
        self.assertEqual(abi, get_contract_def("TokenConversionManagerV2")["abi"])

    def test_fet_sepolia(self):
        abi = get_converter_abi(11155111, "FET", "0xeD3D39b5e2318aA219F51DA57D10a76Dedcc935a")
        self.assertEqual(abi, get_contract_def("TokenConversionManagerV3")["abi"])

    def test_address_and_token_name_case_insensitive(self):
        abi = get_converter_abi(11155111, "agix", "0xFDCDAE14927E8FA6B7490EA855E888A7C957A880")
        self.assertEqual(abi, get_contract_def("TokenConversionManagerV3")["abi"])


class TestGetConverterAbiNegative(unittest.TestCase):
    def test_unknown_token(self):
        with self.assertRaises(ValueError):
            get_converter_abi(1, "ABCDEF", "0x611192364cc6962F433A5dc52cD500A423dd7bE4")

    def test_path_in_token_name(self):
        with self.assertRaises(ValueError):
            get_converter_abi(1, "..", "0xdF8d4826E016aFA8803d94A716FEB70aD5D2B8Ac")

    def test_address_of_another_token(self):
        with self.assertRaises(ValueError):
            get_converter_abi(11155111, "NTX", "0xfdcDAE14927e8fA6b7490Ea855E888a7C957A880")
        with self.assertRaises(ValueError):
            get_converter_abi(11155111, "AGIX", "0xA21784B2Cb386EA6D67DfDaACee5a1a22977c8FC")

    def test_address_from_another_network(self):
        with self.assertRaises(ValueError):
            get_converter_abi(1, "AGIX", "0xfdcDAE14927e8fA6b7490Ea855E888a7C957A880")

    def test_unknown_network(self):
        with self.assertRaises(ValueError):
            get_converter_abi(5, "AGIX", "0xfdcDAE14927e8fA6b7490Ea855E888a7C957A880")

    def test_old_v1_sepolia_converters_removed(self):
        with self.assertRaises(ValueError):
            get_converter_abi(11155111, "AGIX", "0xe8360eeae72facebe6e22aa4fa8bdd7463f4448e")
        with self.assertRaises(ValueError):
            get_converter_abi(11155111, "NTX", "0xf20760E894a1ec1A7bFdaD89d5FBa8aF3d045CCC")


class TestGetContractDeploymentBlockNegative(unittest.TestCase):
    @staticmethod
    def get_w3_without_receipt(network_id: str):
        w3 = mock.MagicMock()
        w3.net.version = network_id
        w3.eth.get_transaction_receipt.side_effect = Exception("Transaction not found")
        return w3

    def test_mainnet_raises(self):
        with self.assertRaises(Exception):
            get_contract_deployment_block(self.get_w3_without_receipt("1"), "SingularityNetToken")

    def test_sepolia_raises(self):
        with self.assertRaises(Exception):
            get_contract_deployment_block(self.get_w3_without_receipt("11155111"), "SingularityNetToken")

    def test_other_network_returns_zero(self):
        self.assertEqual(get_contract_deployment_block(self.get_w3_without_receipt("5"), "SingularityNetToken"), 0)


class TestGetAllAbiContractFiles(unittest.TestCase):
    def test_get_all_abi_contract_files(self):
        contract_files = get_all_abi_contract_files()
        right_length = len(contract_names) == len(contract_files)
        are_all_contracts = all((any((name in str(file)) for name in contract_names)) for file in contract_files)
        self.assertEqual(right_length and are_all_contracts, True)

if __name__ == '__main__':
    unittest.main()
