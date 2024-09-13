# RSA-256 | Cryptography | UTCTF 2024

We are given `vals.txt` which contains an RSA public key and a ciphertext. Simply put the modulus `n` into [factordb.com](http://factordb.com) and use the resulting factorization to compute the private exponent `d` to decrypt the ciphertext.

```py
from Crypto.Util.number import long_to_bytes

n = 77483692467084448965814418730866278616923517800664484047176015901835675610073
p = 1025252665848145091840062845209085931
q = 75575216771551332467177108987001026743883
e = 65537
c = 43711206624343807006656378470987868686365943634542525258065694164173101323321

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
flag = long_to_bytes(m)
print(flag)
```

```
utflag{just_send_plaintext}
```