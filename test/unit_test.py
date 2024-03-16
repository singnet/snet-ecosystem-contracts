import unittest
import sys
sys.path.append(".")

from snet.contracts.utils import *
import web3
from web3.contract import Contract

# Setup for tests
provider = web3.HTTPProvider("https://rpc.tornadoeth.cash/eth")
w3 = web3.Web3(provider)
class_check = False
target_block = 12326815
contract_name = "SingularityNetToken"
address = "0x5B7533812759B45C2B44C19e320ba2cD2681b542"


def test_get_contract_with_name(web3_object, name: str):
    if isinstance(get_contract_object(web3_object, name), Contract):
        return True

def test_get_contract_with_name_and_address(web3_object, name: str, address: str):
    if isinstance(get_contract_object(web3_object, name, address), Contract):
        return True

def test_get_contract_deployment_block_by_contract_name(web3_object, name: str):
    received_block = get_contract_deployment_block(web3_object, name)
    return received_block

# Defining the network by RPC and getting contract instance by contract name
class TestGetContractObjectWithNameOnly(unittest.TestCase):
    """
    Defining the network by RPC and getting contract instance by contract name
    """
    def test_get_contract_with_name(self):
        # Check if the target class has been obtained
        self.assertEqual(test_get_contract_with_name(w3, contract_name), True)


class TestGetContractObjectWithNameAndAddress(unittest.TestCase):
    """
    Defining the network by contract addresss and getting contract instance by contract name
    """
    def test_get_contract_with_name_and_address(self):
        # Check if the target class has been obtained
        self.assertEqual(test_get_contract_with_name_and_address(w3, contract_name, address), True)


class TestGetBlockNumberByContractName(unittest.TestCase):
    """
    Getting contract deployment block by contract_name
    """
    def test_get_deployment_block_by_contract_name(self):
        # Check if the target block has been received
        self.assertEqual(test_get_contract_deployment_block_by_contract_name(w3, contract_name), target_block)

if __name__ == '__main__':
    unittest.main()
