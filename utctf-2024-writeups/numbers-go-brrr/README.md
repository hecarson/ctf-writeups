# numbers go brrr | Cryptography | UTCTF 2024

We are given `main.py` and a command to connect to a server `nc betta.utctf.live 7356`. The server allows us to encrypt arbitrary plaintext using AES in ECB mode, but the key is seemingly randomly generated for every plaintext. The server also allows us to get an encrypted flag.

The random numbers are generated from a seed which only has a range of $10^6$. If we can get the correct seed used by the server, then we will be able to correctly predict all of the subsequent random keys that are used for encryption. To find the seed, we first encrypt an arbitrary plaintext and get the resulting ciphertext from the server. Next, we brute force the seed by enumerating all possible $10^6$ initial seeds and for each guessed seed, generate a key, encrypt our plaintext with the key using AES-ECB, and check whether the resulting ciphertext matches the server ciphertext.

Once we find a seed that produces the same ciphertext as the server, we can get an encrypted flag and predict the key that is used. We decrypt the flag using AES-ECB with our predicted key to get the flag.

The full decryption code is at `decrypt.py`.

```
utflag{deep_seated_and_recurring_self-doubts}
```