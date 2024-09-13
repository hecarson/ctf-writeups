from pwnlib.tubes.remote import remote
import threading

ciphertext = \
    "73ac6b9467204843d5d15c02c04b2a7e597b04c20f18d0de78512b8e06c4d684" + \
    "e127099a07cb7cb7b89818711a54e7ebc3d4567df35e5b5438416854f808e6e7" + \
    "0bd7bb4a5445fba0497bdd11e7b6df0f466ea52c48bf445858c53120f957b976" + \
    "ec1e1a5e7c1ab6c072df8a0cbe0ba84cbd810e2a2d7ea32c317b58378b0b8bed" + \
    "115f9841491791ad05525e6c054a40d6f8eac2dc855964e56e51490712470ee4" + \
    "e68b842251a896da4f02ecc16b4209e89d90e85d4559b7b5e62f4a1f06731887" + \
    "0451a681ca3a3144a3e39627774acc062659903db5cec74962a25eca6538000d" + \
    "1cc02d08c5bb9280d30cea4e586dfd05b69ac852d8d758b26aa00973e13bdc09" + \
    "534f300e507680e568908e9c2a366c9a90b082ea0a15ba6849deb2f27c514b82" + \
    "f0198202de7fa72a03befc1eeb5be6a7a17bd6fa6a97410971496909d09be2f7" + \
    "014f78667b0df5d44bf1b7e9437d013badc8509d62fa5722b1aeeb4c7e68e3ee" + \
    "627b1ef5256baba562e1f90bc627ae62e13f53878d9b7ce2bb5d0ee8de05f494" + \
    "be38647362468d1530d7aee8b1857747aadcfd2e43f67a9489efdd75fe986f9a" + \
    "9c2f686a0af020a59860153b9f646d9699b44ffae0b761d959476e960cb354f0" + \
    "d7264c8da1220c13b9c65cf3a1dfae00844b3db7fc4eee87185ba1e71401598d" + \
    "167a787a54d2d363a04daddcf27225656ef664aabf092feb59c16e39986f31a5" + \
    "9d00ff1ae8f92347d2543d2d5b0e8af0e4e0856df775087b02dc37c1b2e15269" + \
    "bdd85446c9e00ff648f7de40673c4c73145537e77e452a33c2a989990473414e" + \
    "6694d7e94279dafefa66848373f5789d00d6260708a64cb63ce4ac2ad7ca3f8d" + \
    "00259fadee461070923c8dc4ceed1a439f70353ba4e8b26ad87551b24474ab34" + \
    "fe4c80d92acea95adb2adac69fd6965a58ed628495978a05805044a5e00831ff" + \
    "c07e480de9d166df626502346a82c714d52c02163512197e9f3d98f734ceee0b" + \
    "1de173d91a53dbce124a3d968a4e9aa1fe23e818989ae5734f1a2a2de387abd4" + \
    "a9a4d13ef4a47bf50725614d2fcefdd9f37e209e04f9736f2d04029eb80e837d" + \
    "0fe590edf2d2d7d404f1f333968e33fb2b4a2241cf5193dc4bbc0aeedc6cb200" + \
    "cc659691d2d2d1a3456fc8b827b245c997e4336e3e1217d15d4f0f6ee4f2c486" + \
    "09d1a3c53dc868e52dd2b8a11c0ac8ffa90226377a7b0aa082200f92c8258427" + \
    "aab57f919153c56c9dfaa479baf8bfcb65ac9e2bce451aefb2b20fef795e556f" + \
    "da77e2664dc36dca010ab1a1f7ee838ca11264bfa1265dd009818cbb985ce7c3" + \
    "28cb52659a07ed09fd3244a0f2f46602816ca3db74b4fea74261d04a153c3453" + \
    "3fb034bfe4a634fc32087290832c367a2b7943c404d7bdf15b06380c57c1f018" + \
    "221f478b6aefd3e63f381eb84377c141a60df7c3f64a0dec8e87d042dead5b0b" + \
    "df9e97acb4fac853f1fe3780e2a007426af6e086df225f7028f2ed16cdc6e947" + \
    "eb08073fe1705d92359fa32b6ba17c450d8f50902437d722ef0d596f528413c8" + \
    "572d37f84fd0411217ad18b1e0cb21378d87b94a821bceb41ed344764c5be556" + \
    "a126447942d166f6a2159c8f32784f6de7390679c8c411d12b36414679b2cdb1" + \
    "e9848e530458fd650a27d7fc889614bedac0fc15431dddb5555de445e36153bc" + \
    "b1c404782dc4af105d18d4245b3aadf6ec92dee9a7186ba3857a1716bf14a41b" + \
    "2bc1549d9094f17e9a44767501df1c24812e6fb7c20df48d47ea627cfeac77c8" + \
    "dd5a6994650f8736097b7bf2f44dc403a5fea89e5e28db9eefc176c2cdb80603" + \
    "f00c3f7485465daa137d2b851a14208705b3fd8f8b8a3fa845385e49cdee6e0b" + \
    "3a7b7ad9747307d1f30743b844b313c50496f420efbff99bc00d2e8e8b42436e" + \
    "cbcc95060b4656656ea5566e5451114a6e850102aae33c8b7e7a90b68b995372" + \
    "6bcbfbd8de3ec77e131889b6847d4ed88afc73356ef22c29f1b8abee4b0811e2" + \
    "4f4da87a25681ea0b28c74fdf6d2bb2761b2a58a1913de8506d786d66ba5116a" + \
    "5a033118c86aec3b400cdb213ffca2f9c5c1cff1b67d431cff97c28b6f8871a1" + \
    "3f170f07dd8215516b2d87eb0394868685f843686995fb06b95d3a108c8d27f1" + \
    "ee1df604f0f747e8fad32ed1ddfb8dea3ebb81e1b32b3d28a907fe516c54084d" + \
    "a10f12175c5930a4de473575214691d5ddb65ef41281cbcb46563eba05517045" + \
    "eee6fcb921f38e3523aaaf8fbd9f0918fbff3dc7f97a76968b478598af276bc3" + \
    "c37098484d6c96bebeadcea13bc7d99e2a7c38e39965f75cd7993fec9b3acb21" + \
    "2ce8b86e16b74c3e4960c62308df936e9de65fe69f012519d1d2d3cb73c31a01" + \
    "eb8f9ea930e5e51e4d75132140899c0012d4c8a72464422232a9499cd5be1fbf" + \
    "45831adc04dc455a093abdc73fb40295ea175ccf5b80c982d980146d9aa67085" + \
    "f0c7d1f900cb28d2b4b9d053644933c40a06743b4675245f89be885b3baef2e2" + \
    "56b240c5520d71f7fa1079fbb9ba6f89cb6b96fcb6e236f79a82089262dbd1f7" + \
    "c426741baee206d99c77a2eb7323fd6a42edae2290258e3c121963864c52f54b" + \
    "f8ffef3d216004d2e430cc0dbbfda5ec3677ce4f344eab00558fc91d9320f1dc" + \
    "f2ea1a40605a49700ed364d1f8992867154a72b6987d09fac38dd140d68a37a0" + \
    "b5a24b2789c73cd9ea8308eb05cebc0e002937ef1c99fbcfba456ab757be0d9b" + \
    "fa155aafc67473b85ff63cafdfa4ec0406be41d8c8fbf8c135bf9ccc388773aa" + \
    "47a1599febb55c0bcd5c00613dc83138e3d79534d714a4ef594d6eec533ee7c5" + \
    "0a8e9ec76563230474f7f0da1a9d079c5f242989facaee47b556d0b4766fd581" + \
    "b4167029c2d732c0e189e2a37a00a54e43d850d1ba7f5ea5413bda15338783ca" + \
    "8a8bebe4264cdf3c4a927091a1a24c3278141db7be7f8f96873d63bdf8bf85b1" + \
    "89de892ef228d441511eac904cf5dca290fc70d379c768116e221a120fb8e378" + \
    "d8e6f0bb03dd899ba32c815c22d19b2c5e4cd8d367aaefa327aa1608e53007f3" + \
    "6911f9f215ab7fd800ba9807de83482f675cc9db7e667b52031adab70fa5dec4" + \
    "34006f80987f1acd4b4f2f8745cb3a60a49820b6166d135bbff2c9bf7f7ff695" + \
    "174ced6e9eb561caf047201d71d31307a0815f23f8e27d13e99bc580e1a24701" + \
    "97acda11459de2ded7bde440ddee63761e168f5d3b4577bc765dcb568d1fbb23" + \
    "7dc583817cfcf08eca76228928c15bcae6d5c4a542aaa1f14413849f199bffea" + \
    "b8d7271fbac7e7586aaff05f91b082f8f27069c71406a9ef81f98ba41d1fc107" + \
    "37a11491657df0b92e4e2fe7b83f601cb216de21cb266849e79208bcb1c0b437" + \
    "77b9859114b8d1b582dcc26b74566a32a44b8c44461023719f59a75f071d9e33"

BLOCK_SIZE = 16
NUM_THREADS = 20

def xor(a: bytes, b:bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])

ciphertext = bytes.fromhex(ciphertext)
ciphertext_dec = bytearray(len(ciphertext))
plaintext = bytearray(len(ciphertext))

ciphertext_dec_lock = threading.Lock()
plaintext_lock = threading.Lock()

def find_plaintext_blocks(start_block_pos: int, end_block_pos: int):
    with remote("cbc.ctf.csaw.io", 9996) as conn:
        # Decrypt each ciphertext block
        for cur_block_pos in range(start_block_pos, end_block_pos):
            # print(f"cur_block_pos {cur_block_pos}")

            c1 = bytearray(BLOCK_SIZE)
            c2 = ciphertext[cur_block_pos * BLOCK_SIZE : (cur_block_pos + 1) * BLOCK_SIZE]

            # Decrypt each ciphertext byte in the block in reverse order
            for cur_byte_pos in range(BLOCK_SIZE - 1, -1, -1):
                # print(f"cur_byte_pos {cur_byte_pos}")

                # Bytes in c1 from (cur_byte_pos + 1) to (BLOCK_SIZE - 1) need to produce correct padding value in p2
                # This needs to be done before finding decrypted c2 byte at cur_byte_pos
                cur_pad_byte = BLOCK_SIZE - cur_byte_pos
                for i in range(cur_byte_pos + 1, BLOCK_SIZE):
                    c1[i] = ciphertext_dec[cur_block_pos * BLOCK_SIZE + i] ^ cur_pad_byte

                # Find the byte in c1 at cur_byte_pos that produces the correct pad byte in p2
                for cur_c1_byte in range(2**8):
                    c1[cur_byte_pos] = cur_c1_byte

                    conn.recvuntil(b"ciphertext: ")
                    input_line = (c1 + c2).hex().encode()
                    conn.sendline(input_line)
                    line = conn.recvline()
                    if line.startswith(b"Error"):
                        continue

                    c2_dec_byte = cur_c1_byte ^ cur_pad_byte
                    ciphertext_dec_lock.acquire()
                    ciphertext_dec[cur_block_pos * BLOCK_SIZE + cur_byte_pos] = c2_dec_byte
                    ciphertext_dec_lock.release()
                    # print(f"found c2_dec_byte {c2_dec_byte}")
                    break
            
            # Plaintext is decrypted block XOR previous ciphertext block
            p2 = xor(
                ciphertext_dec[cur_block_pos * BLOCK_SIZE : (cur_block_pos + 1) * BLOCK_SIZE],
                ciphertext[(cur_block_pos - 1) * BLOCK_SIZE : cur_block_pos * BLOCK_SIZE]
            )
            print(f"cur_block_pos {cur_block_pos} p2 {p2}")
            plaintext_lock.acquire()
            plaintext[cur_block_pos * BLOCK_SIZE : (cur_block_pos + 1) * BLOCK_SIZE] = p2
            plaintext_lock.release()



num_blocks = len(ciphertext) // BLOCK_SIZE - 1
threads: list[(int, threading.Thread)] = []

for thread_idx in range(NUM_THREADS):
    start_block_idx = (num_blocks * thread_idx) // NUM_THREADS + 1
    end_block_idx = (num_blocks * (thread_idx + 1)) // NUM_THREADS + 1
    t = threading.Thread(target=find_plaintext_blocks, args=(start_block_idx, end_block_idx))
    t.start()
    threads.append((thread_idx, t))
for idx, t in threads:
    t.join()
    print(f"thread {idx} done")

print(plaintext)
