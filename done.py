# turns out we can leverage the guys library.

import blocksmith

key = '7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b741027884d00'

address = blocksmith.BitcoinWallet.generate_address(key)
print(address)