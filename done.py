import blocksmith
from generate import util
key = '7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b741027884d00'
ke2 = '6900000000000000000000000000000000000000000000000000000000000000'
ke3 = '1010101010101010101010101010101010101010101010101010101010101010'

def addr_print(addr: str):
  print('open https://www.blockchain.com/btc/address/%s' % addr)


def input_to_valid_key(input: str):
  input_length = len(input)
  if input_length > 64:
    raise("dodgy input bigger than life!")
  print("gimme gimme gimme")
  
  diff = 64 - input_length
  zero_buffer =  '0' * diff
  return zero_buffer + input

# we want to return a 64 byte string as a 64 element hex array
def gimme_64_byte_hex_array(input: str):
  buffed_input = input_to_valid_key(input)

  # shit code statement below map, join, zip iter!@
  buffed_split = list(map(''.join, zip(*[iter(buffed_input)]*2)))
  
  output = [hex(int(numeric_string, 16)) for numeric_string in buffed_split]
  print(output)
  return output

smol_key = int('1', 16)
test = smol_key.to_bytes(32, byteorder='big')


pub_key = blocksmith.BitcoinWallet.generate_compressed_address(ke3)
print(pub_key)
address = blocksmith.BitcoinWallet.generate_address(ke3)
addr_print(address)



decoded = '00' + str(util.base58_decode(address))
print(decoded)
print(int(decoded))
print(util.base58_encode(decoded))

addr_print(util.base58_encode('001234123412312341239812312301923156789'))

me = gimme_64_byte_hex_array('ff111111fff0f0f0f0f')

me2 = input_to_valid_key('1111')

pub_key = blocksmith.BitcoinWallet.generate_compressed_address(me2)
print(pub_key)
addr_print(pub_key)