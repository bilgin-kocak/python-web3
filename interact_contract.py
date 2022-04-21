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

# for i in range(len(abi_pangolin)):
#     if abi_pangolin[i]['type'] == 'function':
#         print(abi_pangolin[i]['name'] + ": " +
#               abi_pangolin[i]['stateMutability'])

pangolin_address = "0xE54Ca86531e17Ef3616d22Ca28b0D458b6C89106"


# for i in range(len(abi_tj)):
#     if abi_tj[i]['type'] == 'function':
#         print(abi_tj[i]['name'] + ": " + abi_tj[i]['stateMutability'])

trader_joe_address = "0x60aE616a2155Ee3d9A68541Ba4544862310933d4"

contract_tj = w3.eth.contract(address=trader_joe_address, abi=abi_tj)
contract_p = w3.eth.contract(address=pangolin_address, abi=abi_pangolin)

WAVAX = contract_tj.functions.WAVAX().call()
WAVAX = w3.toChecksumAddress(WAVAX)

xava = w3.toChecksumAddress('0xd1c3f94DE7e5B45fa4eDBBA472491a9f4B166FC4')
xava_decimals = 18

usdc = w3.toChecksumAddress('0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E')
usdc_decimals = 6
mim = w3.toChecksumAddress('0x130966628846BFd36ff31a822705796e8cb8C18D')
mim_decimals = 18


xava_wavax_path = [xava, WAVAX]

amountIn = w3.toWei('1', 'ether')


result = contract_tj.functions.getAmountsOut(amountIn, xava_wavax_path).call()
tokenA = result[1]/(10 ** xava_decimals)
print(f"XAVA/WAVAX TraderJoe: {result[1]/(10 ** xava_decimals)}")
result = contract_p.functions.getAmountsOut(amountIn, xava_wavax_path).call()
tokenB = result[1]/(10 ** xava_decimals)
print(f"XAVA/WAVAX TraderJoe: {result[1]/(10 ** xava_decimals)}")

aave_fee = 0.09/100
slippage = 0.1/100

swap_ratio = abs(tokenA - tokenB)/min(tokenA, tokenB)

if swap_ratio > aave_fee + slippage:
    print("Arbitrage opportunity detected!")


wavax_usdc_path = [WAVAX, usdc]
wavax_mim_path = [WAVAX, mim]

amountIn = w3.toWei('1', 'ether')


result = contract_tj.functions.getAmountsOut(amountIn, wavax_usdc_path).call()
tokenA = result[1]/(10 ** usdc_decimals)
print(f"XAVA/WAVAX TraderJoe: {result[1]/(10 ** xava_decimals)}")
result = contract_tj.functions.getAmountsOut(amountIn, wavax_mim_path).call()
tokenB = result[1]/(10 ** mim_decimals)
print(f"XAVA/WAVAX TraderJoe: {result[1]/(10 ** xava_decimals)}")

aave_fee = 0.09/100
slippage = 0.1/100

swap_ratio = abs(tokenA - tokenB)/min(tokenA, tokenB)

initial_fund = 1000  # WAVAX amount
if swap_ratio > aave_fee + slippage:
    print("Arbitrage opportunity detected!")
    kar = initial_fund*(swap_ratio - aave_fee - slippage)  # in wavax
    print("Kar: " + str(kar))


amountIn = w3.toWei('1', 'ether')

amountOutMin = w3.toWei('1', 'ether')

amountA = w3.toWei('1', 'ether')
reserveA = w3.toWei('100', 'ether')
reserveB = w3.toWei('100', 'ether')


res = contract_tj.functions.quote(amountA, reserveA, reserveB).call()
print(w3.fromWei(res, 'ether'))

tokenA = WAVAX
tokenB = w3.toChecksumAddress('0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664')
factory_tj = contract_tj.functions.factory().call()


blizz_token = w3.toChecksumAddress(
    '0x0f34919404a290e71fc6A510cB4a6aCb8D764b24')
usdc_token = w3.toChecksumAddress('0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E')
usdc_decimal = 6

path = [blizz_token, w3.toChecksumAddress(WAVAX)]
path = [w3.toChecksumAddress(WAVAX), usdc_token]

result = contract_tj.functions.getAmountsOut(amountIn, path).call()

print(result[1]/(10 ** 6))

# to = w3.toChecksumAddress('0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664')

# deadline = 500000000000000

# # result = contract_tj.functions.swapExactTokensForTokens(
# #     amountIn, amountOutMin, path, to, deadline).call()
# result = contract_tj.functions.factory().call()

# result = contract_tj.functions.getAmountsOut(amountIn, path).call()
# result = contract_tj.functions.getAmountOut(amountIn, path).call()

# # to ether
# # w3.toWei('1', 'ether')
# # print(w3.fromWei(WAVAX, 'ether'))
