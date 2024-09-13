import subprocess

alphabet = [chr(i) for i in range(0x21, 0x7f)]
encrypt_map = {}
i = 1

for c in alphabet:
    print(f"{i}/{len(alphabet)}")
    i += 1

    input = c.encode() + b'\n'
    _res = subprocess.run("./chall", input=input, capture_output=True)
    with open("output.txt", "rb") as file:
        data = file.read()
    encrypt_map[c] = data

print(encrypt_map)
