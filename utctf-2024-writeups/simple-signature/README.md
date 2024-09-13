# simple signature | Cryptography | UTCTF 2024

We are given a command to connect to a server `nc betta.utctf.live 4374`. Upon connecting and playing around with the inputs, we see that the server provides us with an RSA public key and allows us to get the signature of any arbitary positive integer message, signed with the server's private key. When we choose to stop getting signatures from the server, we are prompted to provide a new correct message and signature pair. Entering a message-signature pair that was previously computed by the server will result in an error.

One strange feature of the server is that in the message signing phase, a message that is inputted multiple consecutive times will produce different signatures. Raising the signatures to the public exponent should reproduce the input messages, and this reveals why the signatures are different. If we try to recover our messages from the signatures, we see that the server will add a counter to the input messages, and that the counter starts at 0 and increases by 1 after every input.

RSA has an attack known as the "blinding" attack that allows us to sign a message without knowing the server's private key (https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf). If we want the correct signature for a message $m$, but the signer refuses to sign $m$, then we can trick the signer into signing a different message $m'$ and use it to get the signature for $m$. We construct $m'$ by picking an arbitrary value $r$.

$$
\begin{align*}
m' &\equiv r^e m \quad (\mathrm{mod}\ N) \\
(m')^d &\equiv (r^e m)^d \equiv r m^d \quad (\mathrm{mod}\ N) \\
(m')^d r^{-1} &\equiv m^d \quad (\mathrm{mod}\ N)
\end{align*}
$$

The full solution code is at `solve.py`.

```
utflag{a1m05t_t3xtb00k_3x3rc153}
```

There is also a silly way to solve/cheese this challenge that I didn't think of during the event. Note that 1 to any power is 1, so to produce a valid message-signature pair, we could enter 0 for the message and 1 for the signature. We enter 0 instead of 1 for the message because the server requires that we request at least one signature, setting the server counter to 1.