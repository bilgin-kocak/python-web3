def get_path_infos(w3):

    xava = w3.toChecksumAddress('0xd1c3f94DE7e5B45fa4eDBBA472491a9f4B166FC4')
    xava_decimals = 18
    usdc = w3.toChecksumAddress('0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E')
    usdc_decimals = 6
    usdce = w3.toChecksumAddress('0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664')
    usdce_decimals = 6
    usdte = w3.toChecksumAddress('0xc7198437980c041c805A1EDcbA50c1Ce5db95118')
    usdte_decimals = 6
    mim = w3.toChecksumAddress('0x130966628846BFd36ff31a822705796e8cb8C18D')
    mim_decimals = 18

    wavax = w3.toChecksumAddress('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')
    wavax_decimals = 18

    qi = w3.toChecksumAddress('0x8729438EB15e2C8B576fCc6AeCdA6A148776C0F5')
    qi_decimals = 18

    tus = w3.toChecksumAddress('0xf693248F96Fe03422FEa95aC0aFbBBc4a8FdD172')
    tus_decimals = 18

    wethe = w3.toChecksumAddress('0x49D5c2BdFfac6CE2BFdB6640F4F80f226bc10bAB')
    wethe_decimals = 18

    cly = w3.toChecksumAddress('0xec3492a2508DDf4FDc0cD76F31f340b30d1793e6')
    cly_decimals = 18

    lost = w3.toChecksumAddress('0x449674B82F05d498E126Dd6615a1057A9c088f2C')
    lost_decimals = 18

    hec = w3.toChecksumAddress('0xC7f4debC8072e23fe9259A5C0398326d8EfB7f5c')
    hec_decimals = 18

    joe = w3.toChecksumAddress('0x6e84a6216eA6dACC71eE8E6b0a5B7322EEbC0fDd')
    joe_decimals = 18

    klo = w3.toChecksumAddress('0xb27c8941a7Df8958A1778c0259f76D1F8B711C35')
    klo_decimals = 18

    token_infos = {
        'xava': {'address': xava, 'decimals': xava_decimals},
        'wavax': {'address': wavax, 'decimals': wavax_decimals},
        'qi': {'address': qi, 'decimals': qi_decimals},
        'usdc': {'address': usdc, 'decimals': usdc_decimals},
        'usdce': {'address': usdce, 'decimals': usdce_decimals},
        'usdte': {'address': usdte, 'decimals': usdte_decimals},
        'mim': {'address': mim, 'decimals': mim_decimals},
        'tus': {'address': tus, 'decimals': tus_decimals},
        'wethe': {'address': wethe, 'decimals': wethe_decimals},
        'cly': {'address': cly, 'decimals': cly_decimals},
        'lost': {'address': lost, 'decimals': lost_decimals},
        'hec': {'address': hec, 'decimals': hec_decimals},
        'joe': {'address': joe, 'decimals': joe_decimals},
        'klo': {'address': klo, 'decimals': klo_decimals},
    }

    tj_paths = {
        'xava-wavax': [xava, wavax],
        'wavax-usdc': [wavax, usdc],
        'wavax-usdce': [wavax, usdce],
        'wavax-usdte': [wavax, usdte],
        'wavax-mim': [wavax, mim],
        'qi-wavax': [qi, wavax],
        'mim-wavax': [mim, wavax],
        'usdc-wavax': [usdc, wavax],
        'usdce-wavax': [usdce, wavax],
        'usdte-wavax': [usdte, wavax],
        'wavax-xava': [wavax, xava],
        'wavax-qi': [wavax, qi],
    }

    p_paths = {
        'xava-wavax': [xava, wavax],
        'wavax-usdc': [wavax, usdc],
        'wavax-usdce': [wavax, usdce],
        'wavax-usdte': [wavax, usdte],
        'qi-wavax': [qi, wavax],
        'usdc-wavax': [usdc, wavax],
        'usdce-wavax': [usdce, wavax],
        'usdte-wavax': [usdte, wavax],
        'wavax-xava': [wavax, xava],
        'wavax-qi': [wavax, qi],
    }

    return token_infos, tj_paths, p_paths
