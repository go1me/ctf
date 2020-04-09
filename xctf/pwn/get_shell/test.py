from pwn import *
context(arch="amd64",os="linux",log_level="debug")

p=remote("111.198.29.45",36320)
#p.recvline()
p.interactive()
