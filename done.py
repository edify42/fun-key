import blocksmith
from generate import util
key = '7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b741027884d00'
ke2 = '6900000000000000000000000000000000000000000000000000000000000000'
ke3 = '1010101010101010101010101010101010101010101010101010101010101010'
print(len(ke2))
smol_key = int('1', 16)
test = smol_key.to_bytes(32, byteorder='big')
print(test)

address = blocksmith.BitcoinWallet.generate_address(ke3)
print("open https://www.blockchain.com/btc/address/" + address)



decoded = '00' + str(util.base58_decode(address))
print(decoded)
print(int(decoded))
print(util.base58_encode(decoded))