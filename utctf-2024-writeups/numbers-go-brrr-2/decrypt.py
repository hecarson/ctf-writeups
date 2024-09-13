from pwnlib.tubes.remote import remote
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES

def get_key_and_next_seed(seed: int) -> tuple[bytes, int]:
    key = bytearray()
    cur_seed = seed
    for i in range(8):
        cur_seed = int(str(cur_seed * cur_seed).zfill(12)[3:9])
        key_part = ( cur_seed % (2 ** 16) ).to_bytes(2, "big")
        key.extend(key_part)
    return bytes(key), cur_seed

with remote("betta.utctf.live", 2435) as conn:
    print(conn.recvline())
    print(conn.recvline())

    success = True
    for i in range(3):
        # Get encrypted message
        print(conn.recvline())
        print(conn.recvline())
        conn.sendline(b"2")
        print(conn.recvline())
        conn.sendline(b"h")
        res = conn.recvline(keepends=False)
        ciphertext = res[32:]
        ciphertext = bytes.fromhex(ciphertext.decode())

        plaintext = pad(b"h", 16)

        print("plaintext", plaintext)
        print("ciphertext", ciphertext)

        # Find key by brute forcing initial seed
        key = None
        for trial_seed in range(10 ** 6):
            if trial_seed % 10_000 == 0:
                print("trial seed", trial_seed)

            trial_key, next_seed = get_key_and_next_seed(trial_seed)
            cipher = AES.new(trial_key, AES.MODE_ECB)
            trial_ciphertext = cipher.encrypt(plaintext)

            if trial_ciphertext == ciphertext:
                key = trial_key
                break
        
        print(conn.recvline())
        conn.sendline(b"1")
        print(conn.recvline())
        print(conn.recvline())
        conn.sendline(key.hex().encode())
        line = conn.recvline()
        print(line)
        if line.startswith(b"That is not"):
            success = False
            break

    if success:
        print(conn.recvline())
