import json
from web3 import Web3
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider('https://api.avax.network/ext/bc/C/rpc'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

print(w3.isConnected())

wallet_address = "0xE4d948c2d5724c9F3d4bB592b3ef2B2B80BD2490"

balance = w3.eth.getBalance(wallet_address)
print(balance/(10 ** 18))
print(w3.fromWei(balance, "ether"))


with open("./trader_joe_abi.json") as f:
    abi_tj = json.load(f)
with open("./pangolin_abi.json") as f:
    abi_pangolin = json.load(f)
# print(abi_tj)

for i in range(len(abi_pangolin)):
    if abi_pangolin[i]['type'] == 'function':
        print(abi_pangolin[i]['name'] + ": " +
              abi_pangolin[i]['stateMutability'])

pangolin_address = "0xE54Ca86531e17Ef3616d22Ca28b0D458b6C89106"


# for i in range(len(abi_tj)):
#     if abi_tj[i]['type'] == 'function':
#         print(abi_tj[i]['name'] + ": " + abi_tj[i]['stateMutability'])

# trader_joe_address = "0x60aE616a2155Ee3d9A68541Ba4544862310933d4"

# contract = w3.eth.contract(address=trader_joe_address, abi=abi_tj)

# WAVAX = contract.functions.WAVAX().call()

# amountIn = w3.toWei('1', 'ether')

# amountOutMin = w3.toWei('1', 'ether')

# path = [w3.toChecksumAddress(
#     '0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664'), w3.toChecksumAddress(WAVAX), ]

# to = w3.toChecksumAddress('0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664')

# deadline = 500000000000000

# # result = contract.functions.swapExactTokensForTokens(
# #     amountIn, amountOutMin, path, to, deadline).call()
# result = contract.functions.factory().call()

# result = contract.functions.getAmountsOut(amountIn, path).call()
# result = contract.functions.getAmountOut(amountIn, path).call()

# # to ether
# # w3.toWei('1', 'ether')
# # print(w3.fromWei(WAVAX, 'ether'))
