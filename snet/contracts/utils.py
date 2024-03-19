import json
import os
from pathlib import PurePath
from typing import Any

from eth_typing import BlockNumber
import web3

from web3.contract.contract import Contract

import snet.contracts as contracts

RESOURCES_PATH = PurePath(os.path.dirname(contracts.__file__)).joinpath("resources")


def get_contract_object(w3: web3.Web3, contract_file: str, address: Any=None) -> Contract:
    with open(RESOURCES_PATH.joinpath("abi", f"{contract_file}.json")) as f:
        abi = json.load(f)
    if address:
        return w3.eth.contract(abi=abi, address=w3.to_checksum_address(address))
    with open(RESOURCES_PATH.joinpath("networks", f"{contract_file}.json")) as f:
        networks = json.load(f)
        address = w3.to_checksum_address(networks[w3.net.version]["address"])
    return w3.eth.contract(abi=abi, address=address)


def get_contract_deployment_block(w3: web3.Web3, contract_file: str) -> BlockNumber | int:
    try:
        with open(RESOURCES_PATH.joinpath("networks", f"{contract_file}.json")) as f:
            networks = json.load(f)
            txn_hash = networks[w3.net.version]["transactionHash"]
        return w3.eth.get_transaction_receipt(txn_hash).blockNumber
    except Exception:
        # TODO Hack as currenlty dependecy is on snet-cli so for test purpose return 0,need to remove dependecies from snet-cli ,currently very tightly coupled with it
        if w3.net.version in [1, 5, 11155111]:
            raise Exception("Transaction hash not found for deployed mpe contract")
        return 0
