# Cryptordle | Cryptography | UTCTF 2024

We are given `main.py` and a command to access a server `nc betta.utctf.live 7496`. We must correctly guess three 5-letter words, using at most 6 guesses per word, to get the flag. If a guess is incorrect, we are given a number to help us get closer to the correct word.

The solution code is at `solve.py`. For each word, 5 fixed guesses are used and each resulting number from a guess is saved. The code then calculates the resulting number for every possible 5-letter answer, and lists out answers that satisfy the constraints from the 5 previous guesses. This is a computationally feasible search space, because $26 ^ 5 = 11\,881\,376$. I looked through the list of candidate answers to find a sensible English word to put in as an answer. This worked well enough to get the flag.

```
utflag{sometimes_pure_guessing_is_the_strat}
```