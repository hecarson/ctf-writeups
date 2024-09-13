# golf | Binary Exploitation | CSAW Qualification CTF 2024

## Initial analysis

We are given a single executable "golf".

```
$ file golf
golf: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=7308872906028530e70e0df769669ce6d69426e7, for GNU/Linux 3.2.0, not stripped
```

The binary is not stripped, making our job easier.

`checksec` comes from the Python `pwntools` package:

```
$ checksec golf
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

Note that PIE is enabled, meaning that ASLR will be enabled.

Using Ghidra produces the following decompilation for the `main` function (some variable names have been changed by me for readability):

```
undefined8 main(void)
{
  long i;
  undefined8 *puVar1;
  byte j;
  undefined8 input;
  undefined8 local_510;
  undefined8 buf2 [0x7e];
  undefined8 buf [0x20];
  code *local_18;
  code *local_10;
  
  j = 0x0;
  setvbuf(stdout,(char *)0x0,0x2,0x0);
  setvbuf(stdin,(char *)0x0,0x2,0x0);
  fflush(stdout);
  fflush(stdin);
  puVar1 = buf;
  for (i = 0x20; i != 0x0; i = i + -0x1) {
    *puVar1 = 0x0;
    puVar1 = puVar1 + (ulong)j * -0x2 + 0x1;
  }
  input = 0x0;
  local_510 = 0x0;
  puVar1 = buf2;
  for (i = 0x7e; i != 0x0; i = i + -0x1) {
    *puVar1 = 0x0;
    puVar1 = puVar1 + (ulong)j * -0x2 + 0x1;
  }
  puts("Welcome to PWN GOLF.");
  printf("Would you like to enter your name? ");
  fgets((char *)&input,0x400,stdin);
  printf("hello: ");
  printf((char *)&input);
  printf("\nAlright! Tell me the address you want to aim at!: ");
  __isoc99_scanf(&DAT_00102094,&local_18);
  local_10 = local_18;
  printf("Ok jumping to that address...");
  (*local_10)();
  return 0x0;
}
```

The two for-loops fill two seemingly arbitrary buffers with zeros. Afterwards, the program prompts for a name, prints it out using `printf`, asks for an address, and jumps execution to that address.

The binary also has a `win` function which is likely the function we need to jump to:

```
void win(void)

{
  system("cat /flag.txt");
  return;
}
```

## Exploitaton

[!NOTE]
We have full control over the string printed by `printf`. How can we exploit this?

[!WARNING]
Answer is below.
