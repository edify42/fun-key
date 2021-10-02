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

The random number `k` above is our private key. As above this number is:
`1 <= k <= n-1`

### links

stole some code here and there. e.g.
[protocoin](https://programtalk.com/vs2/?source=python/10047/protocoin/protocoin/util.py)