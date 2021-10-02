from ecdsa import SigningKey, SECP256k1
import ecdsa
import codecs

string_private_key = int("108d243c9d1b707a6d2716b5b9456e7abbf837fb01624903e4ab430760a71200", 16)
print(string_private_key)
print(2**256 - string_private_key)
new_string = int(1)
print(256/8)
byte_string = new_string.to_bytes(32, byteorder='big')
private_key = str.encode("")
generate = False
if generate:
  private_key = SigningKey.generate(curve=SECP256k1)
  string_private_key = private_key.to_string()
  SigningKey.from_string(string_private_key, curve=SECP256k1)

print(private_key)
print(byte_string.hex())

private_key_bytes = byte_string
# Get ECDSA public key
key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
key_bytes = key.to_string()
key_hex = key_bytes.hex()

print(key_hex)