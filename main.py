from generate import gen
import ecdsa

def main():
  t = gen.BitcoinPrivateKey()
  decimal_t = int.from_bytes(t.to_string(), 'big')
  print("I forgot how to code python!")
  print(decimal_t)
  print(2**256 - decimal_t)
  print(bytes.fromhex("60cf347dbc59d31c1358c8e5cf5e45b822ab85b79cb32a9f3d98184779a9efc2"))

  # pub = gen.BitcoinPublicKey(t.to_string())
  print(t)
  print(t.to_string())
  pub = ecdsa.VerifyingKey.from_string(t.to_string(),
            curve=ecdsa.SECP256k1)
  print(pub)
if __name__ == "__main__":
  main()
