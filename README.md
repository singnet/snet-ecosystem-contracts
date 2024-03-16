# SingularityNET Ecosystem Contracts Package

The package was created to easily work with SingularityNET ecosystem EVM contracts with Python

### Usage
  
Easily get an instance of the contract you need from any SingularityNET product with just one call to one of the functions

Install:
```bash
pip install snet.contracts
```

Usage:
```python
from snet.contracts import get_contract_deployment_block, get_contract_object

import web3

provider = web3.HTTPProvider("https://mainnet.infura.io/v3/")
w3 = web3.Web3(provider)

token_contract_instance = get_contract_object(w3, "SingularityNetToken")
deployed_block = get_contract_deployment_block(w3, "SingularityNetToken")
print("Block:", deployed_block)
```
Result:
```bash
Block: 12326815
```

Optional: get an instance at the contract address
```python
token_contract_instance = get_contract_object(w3, "SingularityNetToken" "0x5B7533812759B45C2B44C19e320ba2cD2681b542")
```

### Tests

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 test/unit_test.py
```
