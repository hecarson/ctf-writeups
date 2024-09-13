# bits and pieces | Cryptography | UTCTF 2024

We are given the file `vals.txt` which contain 3 sets of RSA public keys and ciphertexts. The use of multiple moduli inspires the idea of seeing if any two moduli share a common factor using a GCD algorithm. `n2` and `n3` share a common factor which can be found by computing the GCD of `n2` and `n3`, so those two moduli are now factored.

This leaves `n1` to be factored, but it doesn't share any common factors with `n2` or `n3`. When I ran RsaCtfTool, `n1` was factored by the Hart algorithm, which is based on the Fermat factorization method (https://github.com/RsaCtfTool/RsaCtfTool). Currently, `n1` can also be factored using [factordb.com](http://factordb.com/) since the `n1` factors were added sometime during the competition. I have also included `factor.py` which factors `n1` using the Fermat method.

Now that all three moduli are fully factored, we can compute the private exponent `d` for each RSA public key and decrypt each ciphertext.

```
utflag{oh_no_it_didnt_work_</
3_i_guess_i_can_just_use_stan
dard_libraries_in_the_future}

utflag{oh_no_it_didnt_work_</3_i_guess_i_can_just_use_standard_libraries_in_the_future}
```