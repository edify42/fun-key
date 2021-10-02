from ecdsa import SigningKey, SECP256k1
import ecdsa
import codecs

def max():
  power = 256
  max_val = 2**power
  print("max number yo: ")
  print(max_val)
  test_val = 115792089237316195423570985008687907852837564279074904382605163141518161494337
  # print(max_val) # 115792089237316195423570985008687907853269984665640564039457584007913129639936
  if test_val > max_val:
    print("found ya: " + str(power))

## g() was a learning block which shows how the merged 64byte number represents
# the (x,y) coordinates of the point G provided (hex).
def g():
  # removed 04 from start
  G = "79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8".lower()
  Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
  Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
  G_decimal = int(G, 16)
  G_points = G_decimal.to_bytes(64, byteorder='big') # 32 + 32 bytes
  print("me now")
  gx = G_points[0:32].hex()
  print('0x' + gx == hex(Gx))


smol_key = int(1)
big_key = int(115792089237316195423570985008687907852837564279074904382605163141518161494337-1)
rando_internet_key = "108d243c9d1b707a6d2716b5b9456e7abbf837fb01624903e4ab430760a71200"
string_private_key = int(rando_internet_key, 16) # convert to hex
# print(string_private_key)
# print(2**256 - string_private_key)
new_string = string_private_key
byte_string = new_string.to_bytes(32, byteorder='big')
print('byte_string')
print(byte_string.hex())

private_key = str.encode("")
generate = True
if generate:
  private_key = SigningKey.generate(curve=SECP256k1)
  string_private_key = private_key.to_string()
  blah = SigningKey.from_string(string_private_key, curve=SECP256k1)
  print("new key time: ")
  print(blah.to_pem())


private_key_bytes = string_private_key
print("private key: ")
# Get ECDSA public key
pub_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
pub_key_bytes = pub_key.to_string()
pub_key_hex = pub_key_bytes.hex()

print("length of byte array is:")
print(len(pub_key_bytes))

print("full public key: ")
print(pub_key_hex)

print("pub key x:")
pub_x = pub_key_bytes[0:32].hex()
print(pub_x)

pub_y = pub_key_bytes[33:64].hex()