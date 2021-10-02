# fun key

lets learn about gen generation and elliptic curves!

figuring out what a point on a curve after a few hops means for us fans of
encryption.

bitcoin is poison so it's good to understand why it's so hard to compute the
private key from a public key.

## generate

the [generate](./generate) directory contains our code to generate test private
and public keys

## verify

How can we know whether we have valid key pairs generated?

### btc pages to check keys

if we successfully generate btc valid keys, that's enough to confirm that the
algorithms are right as rain!

[blockchain explorer](https://www.blockchain.com/btc/address/1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD)

[blockcypher with api endpoint](https://www.blockcypher.com/dev/bitcoin/#address-endpoint)

## references

### learning

we have [a file](./script.py) which we can use to learn about details on the
curve **Secp256k1** used.

```text
Obtain the group order n of the curve.
For Secp256k1 this is FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141.

Generate a cryptographically secure random number k between 1 and n-1.
```

Note that `2^255 < n < 2^256`

The random number `k` above is our 'seed' number or **private key**?
As above this number is:
`1 <= k <= n-1`

We then compute the public key (x, y) via:

```text
(x, y) = k*G, where G is the generator point of the secp256k1 curve, which is
0479BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

OR
Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8

```

Worth noting is that because we use ECDSA, the key should be positive and
should be less than the order of the curve. The order of secp256k1 is
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141, which is
pretty big: almost any 32-byte number will be smaller than it.

### links

stole some code here and there. e.g.
[protocoin](https://programtalk.com/vs2/?source=python/10047/protocoin/protocoin/util.py)
[generate private key](https://www.freecodecamp.org/news/how-to-generate-your-very-own-bitcoin-private-key-7ad0f4936e6c/)
[generate bitcoin address]()