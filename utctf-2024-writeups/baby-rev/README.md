# Beginner: Basic Reversing Problem | Reverse Engineering | UTCTF 2024

We are given a `baby-rev` file, which is an ELF 64-bit executable. Run it in GDB and break on `main`. Step into `genkey`. Step over the call to `l1` and inspect the address passed as the first argument to `l1` which is `rbp-0x20`. The address points to a string which is the flag.

```
utflag{i_c4n_r3v!}
```