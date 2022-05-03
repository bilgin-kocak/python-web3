
from lib2to3.pgen2.token import tok_name
from arbitrage_paths import get_path_infos
from connect import w3, contract_tj, contract_p

token_infos, tj_paths, p_paths = get_path_infos(w3)
wavax_decimal = token_infos['wavax']['decimals']
usdc_decimal = token_infos['usdc']['decimals']
wavax = token_infos['wavax']['address']
usdc = token_infos['usdc']['address']
xava = token_infos['xava']['address']
xava_decimal = token_infos['xava']['decimals']
tus = token_infos['tus']['address']
tus_decimal = token_infos['tus']['decimals']
usdce = token_infos['usdce']['address']
usdce_decimal = token_infos['usdce']['decimals']
wethe = token_infos['wethe']['address']
wethe_decimal = token_infos['wethe']['decimals']
cly = token_infos['cly']['address']
cly_decimal = token_infos['cly']['decimals']
lost = token_infos['lost']['address']
lost_decimal = token_infos['lost']['decimals']
hec = token_infos['hec']['address']
hec_decimal = token_infos['hec']['decimals']
joe = token_infos['joe']['address']
joe_decimal = token_infos['joe']['decimals']
klo = token_infos['klo']['address']
klo_decimal = token_infos['klo']['decimals']

# Get flash loan
aave_load_usdc = 100000*10**6


def get_last_price(arb_info):

    for arb in arb_info:
        result = [arb['aave_loan']]
        dexes = arb['dexes']
        paths = arb['paths']
        decimals = arb['decimals']
        for i in range(len(arb['paths'])):
            result = dexes[i].functions.getAmountsOut(
                result[-1], paths[i]).call()

        # print(f'Last money {result[-1]/(10**decimals[-1][-1])}')

        if result[-1] > arb['aave_loan']*1.002:
            print(f'Arbitraj opportunity {result[-1]/(10**decimals[-1][-1])}')
            print(arb)


arb_info = []
aave_loan_usdc = 1000*10**6
aave_loan_avax = 10*10**18
# arb_info.append({
#     'aave_loan': aave_loan_usdc,
#     'paths': [[usdc, wavax, xava],
#               [xava, wavax],
#               [wavax, usdc]],
#     'decimals': [[usdc_decimal, wavax_decimal, xava_decimal],
#                  [xava_decimal, wavax_decimal],
#                  [wavax_decimal, usdc_decimal]],

#     'dexes': [contract_tj, contract_p, contract_tj],
# })

# arb_info.append({
#     'aave_loan': aave_loan_usdc,
#     'paths': [[usdc, wavax],
#               [wavax, xava],
#               [xava, wavax, usdc]],
#     'decimals': [[usdc_decimal, wavax_decimal],
#                  [wavax_decimal, xava_decimal],
#                  [xava_decimal, wavax_decimal, usdc_decimal]],

#     'dexes': [contract_tj, contract_p, contract_tj],
# })

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, xava],
              [xava, wavax]],
    'decimals': [[wavax_decimal, xava_decimal],
                 [xava_decimal, wavax_decimal]],

    'dexes': [contract_tj, contract_p],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, xava],
              [xava, wavax]],
    'decimals': [[wavax_decimal, xava_decimal],
                 [xava_decimal, wavax_decimal]],

    'dexes': [contract_p, contract_tj],
})


arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, usdc],
              [usdc, wavax]],
    'decimals': [[wavax_decimal, usdc_decimal],
                 [usdc_decimal, wavax_decimal]],

    'dexes': [contract_p, contract_tj],
})
arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, usdc],
              [usdc, wavax]],
    'decimals': [[wavax_decimal, usdc_decimal],
                 [usdc_decimal, wavax_decimal]],

    'dexes': [contract_tj, contract_p],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, tus],
              [tus, wavax]],
    'decimals': [[wavax_decimal, tus_decimal],
                 [tus_decimal, wavax_decimal]],

    'dexes': [contract_tj, contract_p],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, tus],
              [tus, wavax]],
    'decimals': [[wavax_decimal, tus_decimal],
                 [tus_decimal, wavax_decimal]],

    'dexes': [contract_p, contract_tj],
})

# arb_info.append({
#     'aave_loan': aave_loan_avax,
#     'paths': [[wavax, usdc, usdce],
#               [usdce, wavax]],
#     'decimals': [[wavax_decimal, tus_decimal],
#                  [tus_decimal, wavax_decimal]],

#     'dexes': [contract_tj, contract_tj],
# })

# arb_info.append({
#     'aave_loan': aave_loan_avax,
#     'paths': [[wavax, usdc, usdce],
#               [usdce, wavax]],
#     'decimals': [[wavax_decimal, tus_decimal],
#                  [tus_decimal, wavax_decimal]],

#     'dexes': [contract_tj, contract_p],
# })

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, wethe],
              [wethe, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_tj, contract_p],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, wethe],
              [wethe, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_p, contract_tj],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, cly],
              [cly, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_p, contract_tj],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, cly],
              [cly, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_tj, contract_tj],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, lost],
              [lost, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_p, contract_tj],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, lost],
              [lost, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_tj, contract_p],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, hec],
              [hec, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_p, contract_tj],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, hec],
              [hec, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_tj, contract_p],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, joe],
              [joe, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_p, contract_tj],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, joe],
              [joe, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_tj, contract_p],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, klo],
              [klo, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_p, contract_tj],
})

arb_info.append({
    'aave_loan': aave_loan_avax,
    'paths': [[wavax, klo],
              [klo, wavax]],
    'decimals': [[wavax_decimal, wethe_decimal],
                 [wethe_decimal, wavax_decimal]],

    'dexes': [contract_tj, contract_p],
})
