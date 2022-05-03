import json
from web3 import Web3
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider('https://api.avax.network/ext/bc/C/rpc'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

with open("./trader_joe_abi.json") as f:
    abi_tj = json.load(f)
with open("./pangolin_abi.json") as f:
    abi_pangolin = json.load(f)

pangolin_address = "0xE54Ca86531e17Ef3616d22Ca28b0D458b6C89106"
trader_joe_address = "0x60aE616a2155Ee3d9A68541Ba4544862310933d4"

contract_tj = w3.eth.contract(address=trader_joe_address, abi=abi_tj)
contract_p = w3.eth.contract(address=pangolin_address, abi=abi_pangolin)
