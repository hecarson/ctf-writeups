from pwnlib.tubes.remote import remote

with remote("betta.utctf.live", 4374) as conn:
    print(conn.recvline()) # "Welcome to the signature generator!"
    print(conn.recvline()) # "This service generates signatures for nonnegative integer messages."
    print(conn.recvline()) # "Today's RSA parameters are:"
    line = conn.recvline() # "n = ..."
    print(line)
    n = int(line[4:])
    line = conn.recvline() # "e = ..."
    print(line)
    e = int(line[4:])

    m = 5
    r = 3
    m2 = (pow(r, e, n) * m) % n
    r_inv = pow(r, -1, n)

    print(conn.recvuntil(b": ")) # "Enter a message as an integer (enter 0 to stop): "
    conn.sendline(str(m2).encode())
    line = conn.recvline() # "Your signature is: ..."
    print(line)
    s2 = int(line[19:])
    
    print(conn.recvuntil(b": ")) # "Enter a message as an integer (enter 0 to stop): "
    conn.sendline(b"0")

    s = (s2 * r_inv) % n

    print(conn.recvline()) # "Now, come up with your own pair!"
    print(conn.recvuntil(b": ")) # "Enter a message: "
    conn.sendline(str(m - 1).encode()) # -1 to correct for server counter
    print(conn.recvuntil(b": ")) # "Enter a signature: "
    conn.sendline(str(s).encode())

    print(conn.recvline()) # "Congrats! Here is the flag: utflag{a1m05t_t3xtb00k_3x3rc153}"